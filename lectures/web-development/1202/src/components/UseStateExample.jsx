import { useState } from "react";

function UseStateExample() {
  //   let count = 0;

  const [count, setCount] = useState(0);

  const increase = () => {
    // count = count + 1;
    setCount((pre) => pre + 1);
    console.log(count);
  };

  return (
    <div>
      <p>{count}</p>
      <button onClick={increase}>증가</button>
    </div>
  );
}

export default UseStateExample;
