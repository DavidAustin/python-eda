;; This file may be used to print gschem schematics from the
;; command line.  Typical usage is:
;;
;;   gschem -p -o mysch.ps -s /path/to/this/file/print.scm mysch.sch
;;
;; The schematic in "mysch.sch" will be printed to the file "mysch.ps"

;; Uncomment these to override defaults when printing from the command line
(output-orientation "landscape")
;(output-type "limits")
;(output-color "enabled")
;(output-text "ps")
(paper-size 11.69 8.27) ; A4

;Note in future, v1.9 of gschem, we need
;(print-paper "A4")
;(print-orientation "landscape")
;http://ftp.geda-project.org/geda-gaf/unstable/v1.9/1.9.1/geda-gaf-1.9.1-NEWS.txt

; You need call this after you call any rc file function
(gschem-use-rc-values)

; filename is specified on the command line
(gschem-postscript "dummyfilename")

(gschem-exit)
