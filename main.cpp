#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;


class Complex {
public:
    double real, imag;
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    Complex operator*(const Complex& other) const {
        return Complex(real * other.real - imag * other.imag,
                       real * other.imag + imag * other.real);
    }
    void print() const {
        if (imag >= 0) cout << real << " + " << imag << "i";
        else           cout << real << " - " << -imag << "i";
    }
};


void task1_1() {
    cout << "======================================" << endl;
    cout << "PART 1 — Task 1.1: Operator Precedence" << endl;
    cout << "======================================" << endl;
    int result = 8 + 4 * 3 - 6 / 2;
    cout << "8 + 4 * 3 - 6 / 2 = " << result << endl;
    int v1 = (8 + 4) * (3 - 6) / 2;
    cout << "(8 + 4) * (3 - 6) / 2 = " << v1 << endl;
    int v2 = 8 + 4 * (3 - 6 / 2);
    cout << "8 + 4 * (3 - 6 / 2) = " << v2 << endl;
    int v3 = ((8 + 4) * 3) - (6 / 2);
    cout << "((8 + 4) * 3) - (6 / 2) = " << v3 << endl;
}


void task1_2() {
    cout << "======================================" << endl;
    cout << "PART 1 — Task 1.2: Complex Overloading" << endl;
    cout << "======================================" << endl;
    Complex a(1, 2), b(3, 4), i_unit(0, 1);
    Complex c = a + b * i_unit;
    cout << "a = "; a.print(); cout << endl;
    cout << "b = "; b.print(); cout << endl;
    cout << "i = "; i_unit.print(); cout << endl;
    cout << "b * i = "; (b * i_unit).print(); cout << endl;
    cout << "a + b * i = "; c.print(); cout << endl;
    cout << "(*) has higher precedence than (+), so b*i is evaluated first." << endl;
}


void task2_1() {
    cout << "======================================" << endl;
    cout << "PART 2 — Task 2.1: Implicit Conversion" << endl;
    cout << "======================================" << endl;
    int ii = 5;
    double d = 3.7;
    float f = 2.1f;
    auto x = ii + d;
    auto y = d / ii;
    auto z = f + ii;
    cout << "i + d (int+double) = " << x << "  [double]" << endl;
    cout << "d / i (double/int) = " << y << "  [double, no truncation]" << endl;
    cout << "f + i (float+int)  = " << z << "  [float]" << endl;
}


void task2_3() {
    cout << "======================================" << endl;
    cout << "PART 2 — Task 2.3: Explicit Casting" << endl;
    cout << "======================================" << endl;
    double dval = 9.8;
    int truncated = (int)dval;
    int rounded   = (int)(dval + 0.5);
    cout << "Original double : " << dval << endl;
    cout << "Truncated (int) : " << truncated << endl;
    cout << "Rounded   (int) : " << rounded << endl;
}


bool check(int x, int& y) {
    return (x > 0) && (++y > 0);
}


void task3_1() {
    cout << "======================================" << endl;
    cout << "PART 3 — Task 3.1: Short-Circuit Eval" << endl;
    cout << "======================================" << endl;
    int y1 = 10;
    cout << "Call check(-1, y) where y=10:" << endl;
    cout << "  Before: y = " << y1 << endl;
    check(-1, y1);
    cout << "  After:  y = " << y1 << "  (unchanged -- short-circuit prevented increment)" << endl;

    int y2 = 10;
    cout << "Call check(5, y) where y=10:" << endl;
    cout << "  Before: y = " << y2 << endl;
    check(5, y2);
    cout << "  After:  y = " << y2 << "  (incremented -- both sides evaluated)" << endl;
}


void deMorgans(bool a, bool b) {
    bool lhs1 = !(a && b),  rhs1 = !a || !b;
    bool lhs2 = !(a || b),  rhs2 = !a && !b;
    cout << "  a=" << a << ", b=" << b << endl;
    cout << "  !(a && b) == !a || !b : " << lhs1 << " == " << rhs1 << " -> " << (lhs1 == rhs1 ? "TRUE" : "FALSE") << endl;
    cout << "  !(a || b) == !a && !b : " << lhs2 << " == " << rhs2 << " -> " << (lhs2 == rhs2 ? "TRUE" : "FALSE") << endl;
}


void task3_2() {
    cout << "======================================" << endl;
    cout << "PART 3 — Task 3.2: De Morgan's Law" << endl;
    cout << "======================================" << endl;
    deMorgans(true,  true);
    deMorgans(true,  false);
    deMorgans(false, true);
    deMorgans(false, false);
}


char gradeIfElse(int score) {
    if      (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else if (score >= 70) return 'C';
    else if (score >= 60) return 'D';
    else                  return 'F';
}


char gradeSwitch(int score) {
    switch (score / 10) {
        case 10: case 9: return 'A';
        case 8:          return 'B';
        case 7:          return 'C';
        case 6:          return 'D';
        default:         return 'F';
    }
}


void task4_1() {
    cout << "======================================" << endl;
    cout << "PART 4 — Task 4.1: Grade Calculator" << endl;
    cout << "======================================" << endl;
    int scores[] = {95, 85, 72, 63, 45};
    for (int s : scores) {
        cout << "Score " << s
             << " -> if-else: " << gradeIfElse(s)
             << "  switch: "   << gradeSwitch(s) << endl;
    }
}


void task4_2() {
    cout << "======================================" << endl;
    cout << "PART 4 — Task 4.2: Loop Comparison" << endl;
    cout << "======================================" << endl;
    cout << "for loop (1-10): ";
    for (int n = 1; n <= 10; n++) cout << n << " ";
    cout << endl;

    cout << "while loop (1-10): ";
    int n = 1;
    while (n <= 10) { cout << n++ << " "; }
    cout << endl;

    cout << "do-while loop (1-10): ";
    n = 1;
    do { cout << n++ << " "; } while (n <= 10);
    cout << endl;

    cout << "Even numbers (for + continue): ";
    for (int k = 1; k <= 10; k++) {
        if (k % 2 != 0) continue;
        cout << k << " ";
    }
    cout << endl;
}


void task4_3() {
    cout << "======================================" << endl;
    cout << "PART 4 — Task 4.3: Multiplication Table" << endl;
    cout << "======================================" << endl;
    for (int r = 1; r <= 5; r++) {
        for (int c = 1; c <= 5; c++) {
            cout << r * c;
            if (r * c < 10) cout << "  ";
            else             cout << " ";
        }
        cout << endl;
    }
}


void task5_1() {
    cout << "======================================" << endl;
    cout << "PART 5 — Task 5.1: goto Loop" << endl;
    cout << "======================================" << endl;
    cout << "goto loop:  ";
    int i = 0;
    loop_start:
        if (i > 5) goto loop_end;
        cout << i++ << " ";
        goto loop_start;
    loop_end:
    cout << endl;

    cout << "for loop:   ";
    for (int k = 0; k <= 5; k++) cout << k << " ";
    cout << endl;
    cout << "(Both produce identical output; for loop is cleaner and safer.)" << endl;
}


void task5_2() {
    cout << "======================================" << endl;
    cout << "PART 5 — Task 5.2: Guarded Commands" << endl;
    cout << "======================================" << endl;
    int a = 7, b = 3;
    cout << "Initial: a=" << a << ", b=" << b << endl;

    bool canSwap   = (a > b);
    bool canDouble = (a <= b);

    if (canSwap && canDouble) {
        if (rand() % 2 == 0) { swap(a, b);  cout << "Guard fired: SWAP" << endl; }
        else                  { a *= 2; b *= 2; cout << "Guard fired: DOUBLE" << endl; }
    } else if (canSwap) {
        swap(a, b);
        cout << "Guard fired: SWAP" << endl;
    } else {
        a *= 2; b *= 2;
        cout << "Guard fired: DOUBLE" << endl;
    }
    cout << "Result: a=" << a << ", b=" << b << endl;
}


int main() {
    srand(static_cast<unsigned int>(time(0)));

    // task1_1();
    // task1_2();
    // task2_1();
    // task2_3();
    // task3_1();
    // task3_2();
    // task4_1();
    // task4_2();
    // task4_3();
    // task5_1();
    task5_2();

    return 0;
}