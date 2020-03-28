; Lab 13: Final Review - Optional Questions

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond
        ((null? curr) #f)
        ((contains? seen-so-far curr) #t)
        (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (cond
    ((null? lst) #f)
    ((eq? (car lst) s) #t)
    (else (contains? (cdr lst) s)))
)

(define-macro (switch expr cases)
    (cons 'cond
        (map
            (lambda (case) (cons (eq? (eval expr) (car case)) (cdr case)))
        cases))
)