; (list-of (* x x) for x in '(3 4 5) if (odd? x))
(define-macro (list-of map-expr for var in lst if filter-expr)
    (list 'map (list 'lambda (list var) map-expr)
        (list 'filter (list 'lambda (list var) filter-expr) lst)))

(define-macro (list-of map-expr for var in lst if filter-expr)
    `(map (lambda (,var) ,map-expr)
        `(filter (lambda (,var) ,filter-expr) ,lst)))

(define-macro (list-of expr for var in lst . args)
    (let
    ((filtered (if (= (length args) 2)
     `(filter (lambda (,var) ,(car (cdr args))) ,lst)
                                  lst)))
      `(map (lambda (,var) ,expr) ,filtered)))