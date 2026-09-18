import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  Sparkles,
  LayoutDashboard,
  PlayCircle,
  History,
  User,
  LogOut,
  Menu,
  X
} from 'lucide-react';

const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const navLinks = [
    { path: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { path: '/interview/setup', label: 'Start Interview', icon: PlayCircle },
    { path: '/history', label: 'History', icon: History },
    { path: '/profile', label: 'Profile', icon: User }
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <header className="sticky top-0 z-50 border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2.5 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-purple-600 to-pink-500 flex items-center justify-center shadow-lg shadow-indigo-500/20 group-hover:scale-105 transition-transform">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <span className="text-xl font-black tracking-tight text-white font-outfit">
                Interview<span className="text-indigo-400">AI</span>
              </span>
              <span className="hidden sm:block text-[10px] text-slate-400 font-mono tracking-wider -mt-1 uppercase">
                AI Coach
              </span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          {isAuthenticated ? (
            <nav className="hidden md:flex items-center gap-1 bg-slate-900/60 p-1.5 rounded-xl border border-slate-800/80">
              {navLinks.map((link) => {
                const Icon = link.icon;
                const active = isActive(link.path);
                return (
                  <Link
                    key={link.path}
                    to={link.path}
                    className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                      active
                        ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    <span>{link.label}</span>
                  </Link>
                );
              })}
            </nav>
          ) : (
            <div className="hidden md:flex items-center gap-3">
              <Link
                to="/login"
                className="text-xs font-semibold text-slate-300 hover:text-white px-4 py-2 rounded-lg transition-colors"
              >
                Log In
              </Link>
              <Link
                to="/register"
                className="text-xs font-semibold bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white px-4 py-2 rounded-xl shadow-lg shadow-indigo-500/25 transition-all transform hover:-translate-y-0.5"
              >
                Get Started Free
              </Link>
            </div>
          )}

          {/* User Menu & Mobile Toggle */}
          <div className="flex items-center gap-3">
            {isAuthenticated && (
              <div className="hidden md:flex items-center gap-3 pl-3 border-l border-slate-800">
                <div className="text-right">
                  <p className="text-xs font-semibold text-slate-200">{user?.name}</p>
                  <p className="text-[10px] text-indigo-400 font-mono">{user?.targetRole}</p>
                </div>
                <button
                  onClick={handleLogout}
                  className="p-2 text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-lg transition-colors"
                  title="Log Out"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            )}

            {/* Mobile Hamburger */}
            <button
              onClick={() => setMobileOpen(!mobileOpen)}
              className="md:hidden p-2 text-slate-400 hover:text-white rounded-lg focus:outline-none"
            >
              {mobileOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileOpen && (
        <div className="md:hidden border-b border-slate-800 bg-slate-950 px-4 py-3 space-y-2">
          {isAuthenticated ? (
            <>
              <div className="px-3 py-2 bg-slate-900 rounded-lg mb-3">
                <p className="text-sm font-semibold text-slate-100">{user?.name}</p>
                <p className="text-xs text-indigo-400">{user?.targetRole} • {user?.experienceLevel}</p>
              </div>
              {navLinks.map((link) => {
                const Icon = link.icon;
                return (
                  <Link
                    key={link.path}
                    to={link.path}
                    onClick={() => setMobileOpen(false)}
                    className="flex items-center gap-3 px-3 py-2 rounded-lg text-sm text-slate-300 hover:bg-slate-900"
                  >
                    <Icon className="w-4 h-4 text-indigo-400" />
                    <span>{link.label}</span>
                  </Link>
                );
              })}
              <button
                onClick={() => {
                  setMobileOpen(false);
                  handleLogout();
                }}
                className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm text-rose-400 hover:bg-rose-500/10"
              >
                <LogOut className="w-4 h-4" />
                <span>Log Out</span>
              </button>
            </>
          ) : (
            <div className="flex flex-col gap-2 pt-2">
              <Link
                to="/login"
                onClick={() => setMobileOpen(false)}
                className="w-full text-center py-2 text-sm font-semibold text-slate-300 bg-slate-900 rounded-lg"
              >
                Log In
              </Link>
              <Link
                to="/register"
                onClick={() => setMobileOpen(false)}
                className="w-full text-center py-2 text-sm font-semibold text-white bg-indigo-600 rounded-lg"
              >
                Get Started Free
              </Link>
            </div>
          )}
        </div>
      )}
    </header>
  );
};

export default Navbar;
