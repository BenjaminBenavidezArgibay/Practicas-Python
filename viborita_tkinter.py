import tkinter as tk
import random

# Configuración de la ventana
root = tk.Tk()
root.title("Snake Game")

# Obtener dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Usar todo el espacio disponible en pantalla
width, height = screen_width, screen_height
root.geometry(f"{width}x{height}")
root.state('zoomed')  # Maximizar ventana

# Crear canvas
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Colores
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

# Configuración del snake
SNAKE_BLOCK = 20
SNAKE_SPEED = 100  # Milisegundos entre actualizaciones (menos es más rápido)

# Ajustar dimensiones del canvas para garantizar alineación con la cuadrícula
width = (width // SNAKE_BLOCK) * SNAKE_BLOCK
height = (height // SNAKE_BLOCK) * SNAKE_BLOCK
canvas.config(width=width, height=height)

# Inicialización del juego
snake = [[width // 2, height // 2]]  # Coordenadas iniciales del cuerpo de la serpiente
SNAKE_DIRECTION = None  # Dirección inicial (None para detener el movimiento)
food_position = [
    random.randint(0, (width // SNAKE_BLOCK) - 1) * SNAKE_BLOCK,
    random.randint(0, (height // SNAKE_BLOCK) - 1) * SNAKE_BLOCK
]

score = 0  # Puntaje inicial
running = False  # Variable para controlar el estado del juego

def reset_game():
    """
    Reinicia el juego a su estado inicial.
    """
    global snake, SNAKE_DIRECTION, food_position, running, score
    snake = [[width // 2, height // 2]]
    SNAKE_DIRECTION = None
    food_position = [
        random.randint(0, (width // SNAKE_BLOCK) - 1) * SNAKE_BLOCK,
        random.randint(0, (height // SNAKE_BLOCK) - 1) * SNAKE_BLOCK
    ]
    score = 0
    running = False
    draw_snake_and_food()

def move_snake():
    """
    Mueve la serpiente, verifica colisiones y actualiza el canvas.
    """
    global snake, food_position, SNAKE_DIRECTION, running, score

    if not running or SNAKE_DIRECTION is None:
        return

    head_x, head_y = snake[-1]
    if SNAKE_DIRECTION == "Left":
        head_x -= SNAKE_BLOCK
    elif SNAKE_DIRECTION == "Right":
        head_x += SNAKE_BLOCK
    elif SNAKE_DIRECTION == "Up":
        head_y -= SNAKE_BLOCK
    elif SNAKE_DIRECTION == "Down":
        head_y += SNAKE_BLOCK

    # Agregar nueva posición de la cabeza
    new_head = [head_x, head_y]
    snake.append(new_head)

    # Verificar si la serpiente come la comida
    if new_head[0] == food_position[0] and new_head[1] == food_position[1]:
        food_position = [
            random.randint(0, (width // SNAKE_BLOCK) - 1) * SNAKE_BLOCK,
            random.randint(0, (height // SNAKE_BLOCK) - 1) * SNAKE_BLOCK
        ]
        score += 10  # Incrementar el puntaje
    else:
        # Quitar el último bloque para que no crezca
        snake.pop(0)

    # Verificar colisión con bordes o consigo misma
    if (head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or
            new_head in snake[:-1]):
        game_over()
        return

    # Verificar si toda la pantalla está ocupada
    if len(snake) == (width // SNAKE_BLOCK) * (height // SNAKE_BLOCK):
        you_win()
        return

    draw_snake_and_food()
    root.after(SNAKE_SPEED, move_snake)

def draw_snake_and_food():
    """
    Dibuja la serpiente, la comida y el puntaje en el canvas.
    """
    canvas.delete("all")
    # Dibujar comida
    canvas.create_rectangle(food_position[0], food_position[1],
                            food_position[0] + SNAKE_BLOCK, food_position[1] + SNAKE_BLOCK,
                            fill=FOOD_COLOR)
    # Dibujar serpiente
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1],
                                segment[0] + SNAKE_BLOCK, segment[1] + SNAKE_BLOCK,
                                fill=SNAKE_COLOR)
    # Mostrar puntaje
    canvas.create_text(10, 10, text=f"Puntaje: {score}", anchor="nw", fill="black", font=("Arial", 16))

def game_over():
    """
    Muestra "GAME OVER" en el canvas y detiene el juego.
    """
    global running
    running = False
    canvas.create_text(width // 2, height // 2, text="GAME OVER",
                       fill="red", font=("Arial", 24, "bold"))
    canvas.create_text(width // 2, (height // 2) + 40, text="Precione Enter para Reiniciar",
                       fill="blue", font=("Arial", 16, "bold"))

def you_win():
    """
    Muestra "YOU WIN" en el canvas y detiene el juego.
    """
    global running
    running = False
    canvas.create_text(width // 2, height // 2, text="YOU WIN",
                       fill="green", font=("Arial", 24, "bold"))
    canvas.create_text(width // 2, (height // 2) + 40, text="Precione Enter para Reiniciar",
                       fill="blue", font=("Arial", 16, "bold"))

def change_direction(new_direction):
    """
    Cambia la dirección de la serpiente evitando movimientos opuestos.
    """
    global SNAKE_DIRECTION, running
    directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
    if directions.get(new_direction) != SNAKE_DIRECTION:
        SNAKE_DIRECTION = new_direction
        if not running:
            running = True
            move_snake()  # Iniciar movimiento si estaba detenido

# Asignar teclas de dirección
root.bind("<Left>", lambda event: change_direction("Left"))
root.bind("<Right>", lambda event: change_direction("Right"))
root.bind("<Up>", lambda event: change_direction("Up"))
root.bind("<Down>", lambda event: change_direction("Down"))
root.bind("<a>", lambda event: change_direction("Left"))
root.bind("<d>", lambda event: change_direction("Right"))
root.bind("<w>", lambda event: change_direction("Up"))
root.bind("<s>", lambda event: change_direction("Down"))
root.bind("<Return>", lambda event: reset_game())

# Iniciar el juego
draw_snake_and_food()
root.mainloop()
