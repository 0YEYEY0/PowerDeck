import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
import string
from cartas import guardar_carta

def main():
    # Configuración básica de Pygame
    pygame.init()
    screen = pygame.display.set_mode((1500, 720), pygame.RESIZABLE)
    pygame.display.set_caption('Crear Carta')


    # Definir colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (0, 0, 255)

    # Fuente
    font = pygame.font.Font(None, 32)

    # Definir lista de razas pre-cargadas y tipos de carta
    razas_oficiales = ['Humano', 'Elfo', 'Orco', 'Dragón', 'Ángel', 'Demonio']
    tipos_carta = ['Ultra-Rara', 'Muy Rara', 'Rara', 'Normal', 'Básica']


    # Clases de componentes
    class DropdownBox:
        def __init__(self, x, y, w, h, options):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = GRAY
            self.text = ''
            self.options = options
            self.selected_option = None
            self.active = False
            self.font = pygame.font.Font(None, 32)
            self.option_rects = [pygame.Rect(x, y + (i + 1) * h, w, h) for i in range(len(options))]

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    for i, option_rect in enumerate(self.option_rects):
                        if option_rect.collidepoint(event.pos):
                            self.selected_option = self.options[i]
                            self.active = False

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            if self.selected_option:
                text_surface = font.render(self.selected_option, True, BLACK)
            else:
                text_surface = font.render('Seleccione', True, BLACK)
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

            if self.active:
                for i, option_rect in enumerate(self.option_rects):
                    pygame.draw.rect(screen, self.color, option_rect)
                    option_surface = self.font.render(self.options[i], True, BLACK)
                    screen.blit(option_surface, (option_rect.x + 5, option_rect.y + 5))

        def get_selected_option(self):
            return self.selected_option


    class InputBox:
        def __init__(self, x, y, w, h, text='', num_only=False):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = GRAY
            self.text = text
            self.num_only = num_only
            self.txt_surface = font.render(text, True, BLACK)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = BLUE if self.active else GRAY

            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if self.num_only:
                            if event.unicode.isdigit() or (event.unicode == '-' and not self.text):
                                self.text += event.unicode
                        else:
                            self.text += event.unicode

                    self.txt_surface = font.render(self.text, True, BLACK)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect, 2)
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

        def get_text(self):
            return self.text


    class ImageButton:
        def __init__(self, x, y, w, h):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = GRAY
            self.image_path = ''

        def open_file_dialog(self):
            Tk().withdraw()
            file_path = askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
            if file_path:
                self.image_path = file_path

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.open_file_dialog()

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect, 2)
            text_surface = font.render("Seleccionar Imagen", True, BLACK)
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        def get_image_path(self):
            return self.image_path


    # Crear cajas de texto y dropdowns
    nombre_box = InputBox(300, 30, 200, 20)
    descripcion_box = InputBox(300, 60, 200, 20)
    raza_dropdown = DropdownBox(300, 90, 200, 20, razas_oficiales)
    tipo_carta_dropdown = DropdownBox(300, 150, 200, 20, tipos_carta)
    turno_poder_box = InputBox(300, 180, 200, 20, num_only=True)
    bonus_poder_box = InputBox(300, 220, 200, 20, num_only=True)

    atributos = [
        "Poder", "Velocidad", "Magia",
        "Defensa", "Inteligencia", "Altura",
        "Fuerza", "Agilidad", "Salto",
        "Resistencia", "Flexibilidad", "Explosividad",
        "Carisma", "Habilidad", "Balance",
        "Sabiduría", "Suerte", "Coordinación",
        "Amabilidad", "Lealtad", "Disciplina",
        "Liderazgo", "Prudencia", "Confianza",
        "Percepción", "Valentía"
    ]

    atributos_boxes = {}
    x_offset = 50
    y_offset = 280
    for i, attr in enumerate(atributos):
        x = x_offset + (i % 3) * 350
        y = y_offset + (i // 3) * 50
        atributos_boxes[attr] = InputBox(x + 190, y, 100, 32, num_only=True)

    image_button = ImageButton(300, 120, 200, 32)

    input_boxes = [
        nombre_box, descripcion_box,
        turno_poder_box, bonus_poder_box
    ] + list(atributos_boxes.values())


    def generar_id_unico(nombre_carta, nombre_variante):
        return "C-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + \
               "-V-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12))


    def validar_datos():
        for box in atributos_boxes.values():
            try:
                valor = int(box.get_text())
                if valor < -100 or valor > 100:
                    return False, f"El valor de {box} debe estar entre -100 y 100."
            except ValueError:
                return False, "Los valores de atributos deben ser números."

        try:
            turno_poder = int(turno_poder_box.get_text())
            bonus_poder = int(bonus_poder_box.get_text())
            if not (0 <= turno_poder <= 100):
                return False, "El turno de poder debe estar entre 0 y 100."
            if not (0 <= bonus_poder <= 100):
                return False, "El bonus de poder debe estar entre 0 y 100."
        except ValueError:
            return False, "Turno de poder y bonus poder deben ser números."

        if raza_dropdown.get_selected_option() is None:
            return False, "Debe seleccionar una raza."
        if tipo_carta_dropdown.get_selected_option() is None:
            return False, "Debe seleccionar un tipo de carta."

        if not image_button.get_image_path():
            return False, "Debe seleccionar una imagen."

        return True, ""


    def draw_labels(screen):
        labels = [
            ("Nombre", (100, 30)),
            ("Descripción", (100, 60)),
            ("Raza", (100, 90)),
            ("Imagen", (100, 120)),
            ("Tipo de Carta", (100, 150)),
            ("Turno Poder", (100, 180)),
            ("Bonus Poder", (100, 220)),
        ] + [(attr, (100 + (i % 3) * 350, 280 + (i // 3) * 50)) for i, attr in enumerate(atributos_boxes.keys())]

        for label, pos in labels:
            text_surface = font.render(label, True, BLACK)
            screen.blit(text_surface, pos)


    running = True
    while running:
        screen.fill(WHITE)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for box in input_boxes:
                box.handle_event(event)

            raza_dropdown.handle_event(event)
            tipo_carta_dropdown.handle_event(event)
            image_button.handle_event(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Validar todos los datos antes de intentar guardar
                es_valido, mensaje_error = validar_datos()

                if es_valido:
                    atributos_valores = {attr: int(box.get_text()) for attr, box in atributos_boxes.items()}
                    try:
                        # Generar ID único para la carta
                        id_unico = generar_id_unico(nombre_box.get_text(), "Principal")  # "Principal" para la variante

                        resultado = guardar_carta(
                            nombre_box.get_text(),
                            descripcion_box.get_text(),
                            "Principal",  # "Principal" para la variante
                            raza_dropdown.get_selected_option(),
                            tipo_carta_dropdown.get_selected_option(),
                            int(turno_poder_box.get_text()),
                            int(bonus_poder_box.get_text()),
                            atributos_valores,
                            image_button.get_image_path()
                        )

                        print("Carta guardada exitosamente:", resultado)
                    except Exception as e:
                        print("Error al guardar la carta:", str(e))

                else:
                    print("Error de validación:", mensaje_error)

        for box in input_boxes:
            box.draw(screen)

        raza_dropdown.draw(screen)
        tipo_carta_dropdown.draw(screen)
        image_button.draw(screen)

        draw_labels(screen)

        pygame.display.flip()

    pygame.quit()
