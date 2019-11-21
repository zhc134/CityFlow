#include "flow/flow.h"
#include "engine/engine.h"


namespace CityFlow {
    void Flow::nextStep(double timeInterval) {
        if (!available) return;
        if (endTime != -1 && currentTime > endTime) return;
        if (currentTime >= startTime) {
            while (nowTime >= interval) {
//                std::cerr << "push vehicle" << std::endl;
                Vehicle *vehicle;
                if (hasRoute) {
                    vehicle = new Vehicle(vehicleTemplate, id + "_" + std::to_string(cnt++), engine, false);
                }
                try {
                    vehicle = new Vehicle(vehicleTemplate, id + "_" + std::to_string(cnt++), engine);
                    vehicleTemplate.route = std::make_shared<Route>(vehicle->controllerInfo.router.getRoute());
                    if (vehicleTemplate.route->getRoute().size() < 10) {
                        std::cerr << "too short" << std::endl;
                        available = false;
                    }
                    hasRoute = true;
                }catch(std::runtime_error e){
                    available = false;
                    return;
                }
                int priority = vehicle->getPriority();
                while (engine->checkPriority(priority)) priority = engine->rnd();
                vehicle->setPriority(priority);
                engine->pushVehicle(vehicle, false);
                vehicle->getFirstRoad()->addPlanRouteVehicle(vehicle);
                nowTime -= interval;
            }
            nowTime += timeInterval;
        }
        currentTime += timeInterval;
    }

    std::string Flow::getId() const {
        return id;
    }

    void Flow::reset() {
        nowTime = interval;
        currentTime = 0;
        cnt = 0;
    }
}