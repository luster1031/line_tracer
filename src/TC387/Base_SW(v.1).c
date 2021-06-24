#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include "sci.h"
#include "IR.h"
#include "sci_polling.h"
#include "mc9s12dp512.h"
#include "Moter.h"

void main(void) {
  /* put your own code here */
   UINT_8 data;
   IR_init();
   MT_Init();
  
  while(TRUE){
    data = IR_data();
    if(data == 3){
        //MT_Stop();
      if(data == 2){
        MT_Hard_Left();
      } else if(data == 1) {
       MT_Hard_Right();
      } else if(data == 0) {
        MT_Forward();
      }
    } else if(data == 2) {     
      MT_Hard_Left();
    } else if(data == 1) {
     MT_Hard_Right();
    } else if(data == 0) {
      MT_Forward();
    }
    
  }
  
}
