(define-macro (while cond body change)
`(if ,cond (begin ,body ,change (while ,cond ,body ,change))))