
int i = 0;
int trials = 100;

// connect sensor 1 to Analog pin A1
int sensor1= A1;
// connect sensor 2 to Analog pin A2
int sensor2= A2;
// connect sensor 3 to Analog pin A3
int sensor3= A3;

void setup()
{
  // Begin Serial Communication at BAUD rate 9600
  Serial.begin(9600);
}


float measure_temp(float sensor)
{
  float val = analogRead(sensor);
  // val to mv -> ( analog_val / 1024.0 ) * 5000
  // mv to celsius -> mv / 10
  return (val/1024.0)*5000 / 10;
} 

void loop()
{
  if (i == 0 ) {
    // initial delay for starting capture    
    delay(1000);
    // flush the serial befor initiating capture    
    Serial.flush();
  }
  for (; i < trials; i++) {
    // Measure Temparature for Each Sensor    
    float cel1 = measure_temp(sensor1);
    float cel2 = measure_temp(sensor2);
    float cel3 = measure_temp(sensor3);
    //Transmit data serially    
    Serial.println(String(cel1)+" "+ String(cel2)+" "+ String(cel3));
    delay(1000);
  }
  if (i == trials) {
   // tramit caputure completion command    
   Serial.println("done");
   Serial.flush();
   i++;
  }
}
