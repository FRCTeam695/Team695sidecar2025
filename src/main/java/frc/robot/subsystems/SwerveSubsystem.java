
/* 
package frc.robot.subsystems;

//imports
import java.lang.Object;
import com.ctre.phoenix6.hardware.TalonFX;
import com.ctre.phoenix6.hardware.CANcoder;

import java.util.function.DoubleSupplier;

import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.RunCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.hal.CANAPIJNI;
import edu.wpi.first.wpilibj.DigitalInput;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;


public class SwerveSubsystem extends SubsystemBase {
    
    public double W;
    public double L;
    public double lastAngle;

    public SwerveSubsystem (double trackWidth, double trackLength){
      W = trackWidth/2;
      L = trackLength/2;
    }

    SwerveModule swerve = new SwerveModule(23, 22, 21, W, L);

    public double deadband(double value){
      double returnValue = value;
      if(Math.abs(value) < 0.05){
        returnValue = 0;
      }
      return returnValue;

    }

    public Command drive(DoubleSupplier forward, DoubleSupplier strafe, DoubleSupplier rotation){

    return new RunCommand(

      ()-> {
        double FWD = deadband(forward.getAsDouble());
        double STR = deadband(strafe.getAsDouble());
        double RCW = deadband(rotation.getAsDouble());


        //THE MATH
        double R = Math.sqrt(L*L + W*W);

        double forward1 = FWD + RCW * (L/R);
        double strafe1 = STR + RCW * (W/R);
        
        double speed = Math.sqrt(forward1*forward1 + strafe1*strafe1);
        double steeringAngle = Math.toDegrees(Math.atan2(strafe1, forward1));

        //if(FWD < 0) speed *= -1;
        //if(RCW < 0) steeringAngle*= -1;

        if(FWD == 0 && STR == 0 && RCW == 0){
          steeringAngle = lastAngle;
        }

        SmartDashboard.putNumber("Speed", speed);
        SmartDashboard.putNumber("Steering Angle", steeringAngle);

        double[] speedAndRotation = {speed, steeringAngle};
        swerve.driver(speedAndRotation);
        lastAngle = steeringAngle;
        },

      this);
  }
}
*/
