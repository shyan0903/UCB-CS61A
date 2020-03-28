(define (accumulate combiner start n term)
    (if (= n 0) start
  (accumulate combiner
    (combiner start (term n)) (- n 1) term))
)

(define (accumulate-tail combiner start n term)
  (if (= n 0) start
  (accumulate combiner
    (combiner start (term n)) (- n 1) term))
)

(define (rle s)
    (define (rle-helper prev count s)
        (cond
            ((null? s) (cons-stream (list prev count) nil))
            ((= (car s) prev) (rle-helper (car s) (+ count 1) (cdr-stream s)))
            (else (cons-stream (list prev count) 
                               (rle-helper (car s) 1 (cdr-stream s))))
        )
    )
    (if (null? s) nil
        (rle-helper (car s) 1 (cdr-stream s)))
)