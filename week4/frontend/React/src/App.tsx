import React  from "react";

import Counter from "./Components/counter";
import List from "./Components/marks";
import Card from "./Components/cards";

function App(){
  return(
    <div>
      <Counter/>

      <hr/>
      <List/>
      <hr/>
      <h1>Details</h1>
      <Card
         Name="Surendra"
         Role="Trainee"
         Company="Genworx"/>
      <Card
          Name="Suri"
          Role="SDE"
          Company="AIRBUS"/>
      <Card
         Name="Manasa"
         Role="Testing"
         Company="O9 Solutions"
         />
      <Card
        Name="Revathi"
        Role="Networks"
        Company="HCL"/>
    </div>
  )
}

export default App;