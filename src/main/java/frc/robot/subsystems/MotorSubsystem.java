/*
package frc.robot.subsystems;

import edu.wpi.first.networktables.BooleanPublisher;
import edu.wpi.first.networktables.DoublePublisher;
import edu.wpi.first.networktables.IntegerPublisher;

//imports
import com.revrobotics.RelativeEncoder;
import com.revrobotics.SparkPIDController;
import com.revrobotics.CANSparkLowLevel.MotorType;
import com.revrobotics.CANSparkMax;

import java.util.function.DoubleSupplier;

import com.revrobotics.CANSparkBase;
import com.revrobotics.CANSparkFlex;
//import com.revrobotics.CANSparkMax.ControlType;
//import com.revrobotics.CANSparkMaxLowLevel;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.wpilibj.DigitalInput;


public class MotorSubsystem extends SubsystemBase{
 
  IntegerPublisher xPub;
  IntegerPublisher yPub;


  BooleanPublisher xButton;
  DoublePublisher xStick;


  CANSparkFlex motor;
  SparkPIDController motorPIDController;


  DigitalInput limitSwitch = new DigitalInput(0);

  //constructor
  public MotorSubsystem()
  {
    motor = new CANSparkFlex(56, MotorType.kBrushless);
    motorPIDController = motor.getPIDController();
    
    // Set the setpoint of the PID controller in raw position mode
    motorPIDController.setReference(0.1, CANSparkBase.ControlType.kPosition);
    motorPIDController.setP(0.0003);
    motorPIDController.setI(0.000001);
    motorPIDController.setD(0.00001);

    // Set the minimum and maximum outputs of the motor [-1, 1]
    motorPIDController.setOutputRange(-1, 1);
    motorPIDController.setFF(0.0001);
    motor.set(0);
    
  }

*/
//commands start here

  /*
   * when game controller button A is pressed change color to green
   
  public Command runMotor(DoubleSupplier joystick)
  {
    return new FunctionalCommand(

      // ** INIT
      ()-> testInit(),
     
      // ** EXECUTE
      ()-> {
        double value = joystick.getAsDouble();
        if(Math.abs(value) <= 0.1){
          value = 0;
        }
        //limit switch is false when pressed down
        if (!limitSwitch.get()) {
          motor.set(0);
        } else {
          motor.set(value);
        }
      },
     
      // ** ON INTERRUPTED
      interrupted-> {
        motor.set(0);
      },
     
      // ** END CONDITION
      ()-> testEndCondition(),


      // ** REQUIREMENTS
      this);

  }
  
  
  private void testInit()
  {
  }


  private boolean testEndCondition()
  {
    return(false);
  }


  public Command buttonLimitSwitch()
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
    motor.set(0.3);
  }


  private void testInterrupt1()
  {
    motor.set(0);
  }


  private boolean testEndCondition1()
  {
    if(!limitSwitch.get()){
      return true;
    }
    return false;
  }

  @Override
  public void simulationPeriodic() {
    // This method will be called once per scheduler run during simulation
  }
}
*/