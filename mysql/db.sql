-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 26-09-2020 a las 01:57:59
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flavucros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `channels`
--

CREATE TABLE `channels` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `channels`
--

INSERT INTO `channels` (`id`, `name`, `description`, `user_id`) VALUES
(1, 'welcome', NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `channel_messages`
--

CREATE TABLE `channel_messages` (
  `id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `messages` text NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `channel_messages`
--

INSERT INTO `channel_messages` (`id`, `channel_id`, `user_id`, `messages`, `created`) VALUES
(52, 1, 2, 'Escribe el mensaje', '2020-09-26 01:19:35'),
(53, 1, 2, 'Escribe el mensaje', '2020-09-26 01:20:49'),
(54, 1, 2, 'asdf', '2020-09-26 01:20:52');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `channel_users`
--

CREATE TABLE `channel_users` (
  `id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `email`, `password`) VALUES
(1, 'admin@admin.com', '$2a$12$lt9zUQgqOFb25dkfs3ldWOefZHj7M6n2wrjq.6az6QQ1XDOCL4Ytq'),
(2, 'fcarrizalest@gmail.com', '$2a$12$lt9zUQgqOFb25dkfs3ldWOefZHj7M6n2wrjq.6az6QQ1XDOCL4Ytq');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `channels`
--
ALTER TABLE `channels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `index_for_name` (`name`);

--
-- Indices de la tabla `channel_messages`
--
ALTER TABLE `channel_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `channel_users`
--
ALTER TABLE `channel_users`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `index_for_email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `channels`
--
ALTER TABLE `channels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `channel_messages`
--
ALTER TABLE `channel_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT de la tabla `channel_users`
--
ALTER TABLE `channel_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
