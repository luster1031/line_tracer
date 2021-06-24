#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include "sci.h"
#include "IR.h"
#include "sci_polling.h"
#include "mc9s12dp512.h"
#include "Moter.h"

#define MAX_STRING 15
#define int_enable()  {asm andcc   #0xEF;}	  //interrupts enabled
#define int_disable() {asm orcc    #0x10;}	  //interrupts disabled
// buffer for SCI
char sci_rx_buffer[MAX_STRING+1];
char sci_tx_buffer[MAX_STRING*2];

void Delay(const int n){
  unsigned int counter, i;
  for (i = 0; i < n; i++) {
    for (counter = 1; counter != 0; counter++);
  }
}
void main(void) {
  /* put your own code here */
   UINT_8 data;
   IR_init();
   MT_Init();
  //int_enable();
  init_sci0(19200, sci_rx_buffer, MAX_STRING);
  //int_disable()
  
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
