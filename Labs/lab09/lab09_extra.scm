;; Extra Scheme Questions ;;


(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (filter-lst f lst)
  (if (null? lst)
      ()
      (if (f (car lst))
           (cons (car lst) (filter-lst f (cdr lst)))
           (filter-lst f (cdr lst)))))

(define (remove item lst)
  (filter-lst (lambda (x) (not (equal? x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if (null? s)
       ()
       (cons (car s) (no-repeats (remove (car s) (cdr s)))))
)

(define (substitute s old new)
  (cond
      ((null? s) ())
      ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
      ((equal? (car s) old) (cons new (substitute (cdr s) old new)))
      (else (cons (car s) (substitute (cdr s) old new))))
)

(define (sub-all s olds news)
  (if (or (null? s) (null? olds))
      s
      (sub-all (substitute s (car olds) (car news))
               (cdr olds) (cdr news)))
)