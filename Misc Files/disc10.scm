(define (naturals n)
    (cons-stream n (naturals (+ n 1))))

(define (slice s start end)
    (cond
        ((or (null? s) (= end 0)) nil)
        ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
        (else (cons (car s) (slice (cdr-stream s) (- start 1) (- end 1))))))

(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys)) nil
        (cons-stream (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define factorials
    (cons-stream 1 (combine-with * factorials (naturals 1))))

(define fibs
    (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))


(define (exp x)
    (let ((xs (cons-stream x xs))
          (ys (combine-with /
              (combine-with expt xs (naturals 0)) factorials)))
    (combine-with +
        (cons-stream 0 ys) ys)))
(define (exp x)
    (let ((terms (combine-with (lambda (m n) (/ (expt x m) n)
                                (cdr-stream (naturals 0))
                                (cdr-stream factorials)))))
    (cons-stream 1 (combine-with + terms (exp x)))))