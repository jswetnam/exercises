#include "stdio.h"
#include "stdbool.h"

typedef enum {
    EMPTY, CIRCLE, SQUARE
} value_t;

bool SomeoneHasWon(value_t B[][3]) {
    // Check rows
    for (int i = 0; i < 3; ++i) {
        if (B[i][0] != EMPTY) {
            if (B[i][1] == B[i][0] && B[i][2] == B[i][0])
                return true;
        }
    }
    // Check columns
    for (int j = 0; j < 3; ++j) {
        if (B[0][j] != EMPTY) {
            if (B[1][j] == B[0][j] && B[2][j] == B[0][j])
                return true;
        }
    }

    // Check diagonals

    if (B[0][0] != EMPTY) {
        if (B[1][1] == B[0][0] && B[2][2] == B[0][0])
            return true;
    }

    if (B[2][0] != EMPTY) {
        if (B[1][1] == B[2][0] && B[0][2] == B[2][0])
            return true;
    }

    return false;
}

int main() {
    value_t circle_wins_row[][3] = {{EMPTY, SQUARE, CIRCLE},
        {CIRCLE, CIRCLE, CIRCLE},
        {EMPTY, SQUARE, SQUARE}};
    value_t square_wins_diag[][3] = {{SQUARE, SQUARE, CIRCLE},
        {CIRCLE, SQUARE, CIRCLE},
        {EMPTY, CIRCLE, SQUARE}};
    value_t no_one_wins[][3] = {{EMPTY, EMPTY, CIRCLE},
        {CIRCLE, EMPTY, CIRCLE},
        {EMPTY, CIRCLE, EMPTY}};

    if (SomeoneHasWon(circle_wins_row)) {
        puts("Someone Won!");
    }

    if (SomeoneHasWon(square_wins_diag)) {
        puts("Someone Won!");
    }

    if (SomeoneHasWon(no_one_wins)) {
        puts("Someone Won!");
    }

    return 0;

}
