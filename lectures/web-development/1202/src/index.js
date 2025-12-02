import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

// React
// facebook(현 Meta)에서 2013년 개발한 JavaScript UI 라이브러리 입니다.

// 사용자 인터페이스(UI)를 만들기 위한 도구
// HTML처럼 생겼지만 JavaScript의 강력함을 가진 JSX 문법 사용
// 페이지 전체를 새로고침하지 않고도 필요한 부분만 업데이트 가능
// 현재 가장 인기있는 프론트엔드 라이브러리 중 하나

// 문제점
// 코드가 여기저기 흩어져 있어 관리하기 어려움
// UI 상태를 직접 조작해야 함 (명령적)
// 버그가 생기면 어디서 문제가 생겼는지 찾기 어려움
// 코드가 길어지면 유지보수가 악몽이 됨....

// React 장점
// 상태(Like, isLiked)가 변경되면 React가 자동으로 UI를 업데이트
// 코드가 한곳에 모여 있어 이해하기  쉬움
// "UI가 어떻게 보여야 하는지"만 선언하면 됨

// 특징 1 컴포넌트 기반 개발
// 레고 - 완성작품 => 하나의 블록
// 각 블록은 독립적이고, 여러 블록들을 조합하면 큰 구조물을 만들수 있다.

// 재사용 가능: Button 컴포넌트를 만들면 어디서든 사용 가능
// 관리 쉬움: 각 컴포넌트는 자기 일만 하면 됨
// 협업 용이: 팀원 A는 Header, 팀원 B는 Footer 작업 가능
// 테스트 쉬움: 각 컴포넌트를 독립적으로 테스트
