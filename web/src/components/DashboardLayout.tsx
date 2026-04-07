import React from 'react';
export const DashboardLayout = ({ children }) => (
  <div className="flex h-screen bg-slate-900 text-white">
    <aside className="w-64 border-r border-slate-800">Sidebar</aside>
    <main className="flex-1 overflow-auto">{children}</main>
  </div>
);
