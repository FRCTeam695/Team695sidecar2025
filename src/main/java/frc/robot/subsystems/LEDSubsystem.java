// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.


package frc.robot.subsystems;


import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;


import java.util.function.DoubleSupplier;


import edu.wpi.first.networktables.BooleanPublisher;
import edu.wpi.first.networktables.DoublePublisher;
import edu.wpi.first.networktables.IntegerPublisher;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.AddressableLED;
import edu.wpi.first.wpilibj.AddressableLEDBuffer;
import edu.wpi.first.wpilibj.DriverStation;
import edu.wpi.first.wpilibj.Servo;
import edu.wpi.first.wpilibj.Timer;


public class LEDSubsystem extends SubsystemBase {

  private int cnt = 0;
  private int maxcnt = 50;
  private int x = 0, y = 0;
  private int xinc = 1, yinc = 1;


  NetworkTableInstance inst;
  NetworkTable table;
 
  IntegerPublisher xPub;
  IntegerPublisher yPub;

  BooleanPublisher xButton;
  DoublePublisher xStick;


  AddressableLED myled;
  AddressableLEDBuffer my_ledBuffer;
  
  Servo myServo;

  Timer timer;

  //constructor
  public LEDSubsystem()
  {
    inst = NetworkTableInstance.getDefault();
    table = inst.getTable("frc695_test_table");


    xPub = table.getIntegerTopic("x").publish();
    xPub.set(0);


    yPub = table.getIntegerTopic("y").publish();
    yPub.set(0);


    xButton = table.getBooleanTopic("xButton").publish();
    xButton.set(false);


    xStick = table.getDoubleTopic("xStick").publish();
    xStick.set(0);

    myled = new AddressableLED(1);
    my_ledBuffer = new AddressableLEDBuffer(5);

    myled.setLength(my_ledBuffer.getLength());
    
    // Set the data
    myled.setData(my_ledBuffer);
    myled.start();
    
    myServo = new Servo(0);
    timer = new Timer();
  }


  /**
   * Example command factory method.
   *
   * @return a command
   */
  public Command exampleMethodCommand() {
    // Inline construction of command goes here.
    // Subsystem::RunOnce implicitly requires `this` subsystem.
    return runOnce(
        () -> {
          /* one-time action goes here */
        });
  }
  

  //set all LEDs to green
  public void greenLED(){
    for (var i = 0; i < my_ledBuffer.getLength(); i++) {
      // Sets the specified LED to the RGB values for red
      my_ledBuffer.setRGB(i, 0, 255, 0);
   }
   
   myled.setData(my_ledBuffer);
  }


  //set all LEDs to red
  public void redLED(){
    for (var i = 0; i < my_ledBuffer.getLength(); i++) {
      // Sets the specified LED to the RGB values for red
      my_ledBuffer.setRGB(i, 255, 0, 0);
   }
   
   myled.setData(my_ledBuffer);
  }

  //turn off all LEDs
  public void offLED(){
    for (var i = 0; i < my_ledBuffer.getLength(); i++) {
      // Sets the specified LED to the RGB values for red
      my_ledBuffer.setRGB(i, 0, 0, 0);
   }
   
   myled.setData(my_ledBuffer);
  }
  
  /*
   * when game controller button A is pressed change color to green
   */
  public Command greenLEDCommand()
  {
    return new FunctionalCommand(


      // ** INIT
      ()-> testInit2(),
     
      // ** EXECUTE
      ()-> testExecute2(),
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt2(),
     
      // ** END CONDITION
      ()-> testEndCondition2(),


      // ** REQUIREMENTS
      this);

  }
  
  
  private void testInit2()
  {
  }


  private void testExecute2()
  {
    greenLED();
  }


  private void testInterrupt2()
  {
    offLED();
  }


  private boolean testEndCondition2()
  {
    return(false);
  }


  
  /*
   * when game controller button B is pressed change color to red
   */
  public Command redLEDCommand()
  {
    return new FunctionalCommand(


      // ** INIT
      ()-> testInit1(),
     
      // ** EXECUTE
      ()-> testExecute1(),
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt1(),
     
      // ** END CONDITION
      ()-> testEndCondition1(),


      // ** REQUIREMENTS
      this);


  }
  
  
  private void testInit1()
  {

  }


  private void testExecute1()
  {
    redLED();
  }


  private void testInterrupt1()
  {
    offLED();
  }


  private boolean testEndCondition1()
  {
    return(false);
  }



  /*
   * run servo
   
  public Command redGreenJoystick(DoubleSupplier yVal)
  {
    return new FunctionalCommand(

      // ** INIT
      ()-> testInit4(),
     
      // ** EXECUTE
      ()-> {
        double value = yVal.getAsDouble();
        if(value >= 0){
          redLED();
        } else {
          greenLED();
        }
        myServo.set(value / 2 + 0.5);
      },
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt4(),
     
      // ** END CONDITION
      ()-> testEndCondition4(),


      // ** REQUIREMENTS
      this);
  }

  
  public void testInit4(){
    
  }


  private void testInterrupt4()
  {
    myServo.set(0.475);
    for (var i = 0; i < my_ledBuffer.getLength(); i++) {
      // Sets the specified LED to the RGB values for red
      my_ledBuffer.setRGB(i, 0, 0, 0);
   }
   
   myled.setData(my_ledBuffer);
  }

  private boolean testEndCondition4()
  {
    return(false);
  }
*/

public Command servoToLED(DoubleSupplier yVal)
  {
    return new FunctionalCommand(

      // ** INIT
      ()-> testInit4(),
     
      // ** EXECUTE
      ()-> {
        double yValue = yVal.getAsDouble();
        if(Math.abs(yValue) <= 0.1){
          yValue = 0;
        }
        int numOfLEDs = (int)(Math.abs(yValue) * 5);

        if(yValue >= 0){
          for (var i = 0; i < my_ledBuffer.getLength(); i++) {
            if(i < numOfLEDs)
              my_ledBuffer.setRGB(i, 255, 0, 0);
            else
              my_ledBuffer.setRGB(i, 0, 0, 0);
          } 
        } else {
          for (var i = 0; i < my_ledBuffer.getLength(); i++) {
            if(i < numOfLEDs)
              my_ledBuffer.setRGB(i, 0, 255, 0);
            else
              my_ledBuffer.setRGB(i, 0, 0, 0);
          } 
        }
        
        myled.setData(my_ledBuffer);
        myServo.set(yValue / 2 + 0.5);

      },
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt4(),
     
      // ** END CONDITION
      ()-> testEndCondition4(),


      // ** REQUIREMENTS
      this);
  }

  
  public void testInit4(){
    
  }


  private void testInterrupt4()
  {
    myServo.set(0.475);
    for (var i = 0; i < my_ledBuffer.getLength(); i++) {
      // Sets the specified LED to the RGB values for red
      my_ledBuffer.setRGB(i, 0, 0, 0);
   }
   
   myled.setData(my_ledBuffer);
  }

  private boolean testEndCondition4()
  {
    return(false);
  }

  @Override
  public void periodic() {


    if (DriverStation.isTeleopEnabled() == true)
    {


    // This method will be called once per scheduler run
    if (++cnt == maxcnt)
    {


      cnt = 0;
      x = x + xinc;
      if (x == 40)
      {
        xinc = xinc * -1;
      }
      if (x == 0)
      {
        xinc = xinc * -1;
      }
      y = y + yinc;
      if (y == 30)
      {
        yinc = yinc * -1;
      }
      if (y == 0)
      {
        yinc = yinc * -1;
      }
      xPub.set(x);
      yPub.set(y);
    }


  }
  }


  @Override
  public void simulationPeriodic() {
    // This method will be called once per scheduler run during simulation
  }
}
