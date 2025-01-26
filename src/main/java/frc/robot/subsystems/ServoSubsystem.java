
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
import edu.wpi.first.wpilibj.DriverStation;
import edu.wpi.first.wpilibj.Servo;
import edu.wpi.first.wpilibj.Timer;


public class ServoSubsystem extends SubsystemBase {
  
  //instance variables
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

  Servo myServo;

  Timer timer;


  //constructor
  public ServoSubsystem()
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


    myServo = new Servo(0);
    timer = new Timer();
  }



//commands start here

  /*
   * run servo
   */
  public Command runServoC(DoubleSupplier yVal)
  {
    return new FunctionalCommand(


      // ** INIT
      ()-> testInit3(),
     
      // ** EXECUTE
      ()-> {
        double value = yVal.getAsDouble();
        myServo.set(value / 2 + 0.5);
      },
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt3(),
     
      // ** END CONDITION
      ()-> testEndCondition3(),


      // ** REQUIREMENTS
      this);


  }
  
  
  private void testInit3()
  {

  }


  private void testInterrupt3()
  {
    myServo.set(0.475);
  }


  private boolean testEndCondition3()
  {
    return(false);
  }
  
  /*
   * run servo
   */
  public Command runServoCC(double runtime)
  {
    return new FunctionalCommand(

      // ** INIT
      ()-> testInit0(),
     
      // ** EXECUTE
      ()-> testExecute0(),
     
      // ** ON INTERRUPTED
      interrupted-> testInterrupt0(),
     
      // ** END CONDITION
      ()-> testEndCondition0(runtime),


      // ** REQUIREMENTS
      this);


  }
  
  
  public void testInit0(){
    timer.start();
  }


  private void testExecute0()
  {
    myServo.set(1);
  }


  private void testInterrupt0()
  {
    myServo.set(0.475);
  }

  private boolean testEndCondition0(double runtime)
  {
    if(timer.hasElapsed(runtime)){
      return true;
    }
    return false;
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
