; ; Scheme ;;
(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let 
        ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

;;(define (f f g)
;;  (
; ;   (define zipper
; ;       (lambda (x) (lambda (y a) (x (y (f (g a)))))))
; ;  ((zipper (lambda (p) (+ p 1)))
; ;   (lambda (q) (* q 2)) 9)))

;;(f (lambda (x) x) (lambda (x) x))
