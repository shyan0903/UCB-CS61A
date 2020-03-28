


(define-macro (def func bindings body)
    `(define ,func (lambda ,bindings ,body)))


(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2)))

(define (flatmap f x)
    (if (null? x)
        nil
  (append (f (car x)) (flatmap f (cdr x)))))

(define (expand lst)
  (cond
      ((null? lst) nil)
      ((equal? 'x (car lst)) (append '(x r y f r) (expand (cdr lst))))
      ((equal? 'y (car lst)) (append '(l f x l y) (expand (cdr lst))))
      (else (cons (car lst) (expand (cdr lst))))))

(define (interpret instr dist)
  (cond
      ((null? instr) dist)
      (())))

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))