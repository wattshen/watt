;; The first three lines of this file were inserted by DrScheme. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |11|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(define (area r)
  (* 3.14 r r)
  )
(define (a2 out in)
  (-(area out) (area in))
  )
(a2 5 3)
;;;;;;
(define (profit price)
  (-(revenue price)
    (cost price)))
(define (num_ticket price)
  (+ 120 (*(/(- 5 price) 0.1) 15))
)
(define (revenue price)
  (* (num_ticket price) price)
  )

(define (cost price)
  (+ 180 (* 0.04 (num_ticket price)))
 )


(profit 4)
(num_ticket 4)
(revenue 4)
(cost 4)