from chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        from_row = int(input("From row: "))
        from_col = int(input("From column: "))
        to_row = int(input("To row: "))
        to_col = int(input("To column: "))
        chess.move(from_row, from_col, to_row, to_col)
        print(chess.show_board())
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()