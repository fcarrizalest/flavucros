-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 25-09-2020 a las 02:25:18
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
-- Estructura de tabla para la tabla `channel_messages`
--

CREATE TABLE `channel_messages` (
  `id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `messages` text NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `channel_messages`
--

INSERT INTO `channel_messages` (`id`, `channel_id`, `messages`, `created`) VALUES
(1, 1, 'Escribe el mensaje', '2020-09-25 02:00:47'),
(2, 1, 'Escribe el mensaje', '2020-09-25 02:00:51'),
(3, 1, 'Escribe el mensaje', '2020-09-25 02:03:35'),
(4, 1, 'Escribe el mensaje', '2020-09-25 02:03:56'),
(5, 1, 'Escribe el mensaje', '2020-09-25 02:04:46'),
(6, 1, 'Escribe el mensaje', '2020-09-25 02:05:47'),
(7, 1, 'Escribe el mensaje', '2020-09-25 02:05:50'),
(8, 1, 'Escribe el mensaje', '2020-09-25 02:06:25'),
(9, 1, 'Escribe el mensaje', '2020-09-25 02:06:28'),
(10, 1, 'Escribe el mensaje', '2020-09-25 02:07:04'),
(11, 1, 'Escribe el mensaje', '2020-09-25 02:07:29'),
(12, 1, 'Escribe el mensaje', '2020-09-25 02:08:07'),
(13, 1, 'Escribe el mensaje', '2020-09-25 02:08:09'),
(14, 1, 'Escribe el mensaje', '2020-09-25 02:08:10'),
(15, 1, 'Escribe el mensaje', '2020-09-25 02:08:10'),
(16, 1, 'Escribe el mensaje', '2020-09-25 02:08:10'),
(17, 1, 'Escribe el mensaje', '2020-09-25 02:08:10'),
(18, 1, 'Escribe el mensaje', '2020-09-25 02:10:05'),
(19, 1, 'Escribe el mensaje', '2020-09-25 02:10:07'),
(20, 1, 'Escribe el mensaje', '2020-09-25 02:10:33'),
(21, 1, 'asdf', '2020-09-25 02:10:36'),
(22, 1, 'asdf 1', '2020-09-25 02:10:38'),
(23, 1, 'tw', '2020-09-25 02:10:41'),
(24, 1, 'jajaja', '2020-09-25 02:18:10'),
(25, 1, 'Xd', '2020-09-25 02:20:37'),
(26, 1, 'tw', '2020-09-25 02:20:48'),
(27, 1, 'qqq', '2020-09-25 02:22:09'),
(28, 1, 'Escribe el mensaje', '2020-09-25 02:24:45');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `channel_messages`
--
ALTER TABLE `channel_messages`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `channel_messages`
--
ALTER TABLE `channel_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
