# DB2ADMIN.ABSCALENDARAUTH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CTYPE`, `CALENDARID`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117558

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CALENDARID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `AUTHVIEW` | SMALLINT | NOT NULL |  |  |  |
| 5 | `AUTHCREATE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCALENDAR_AUTHS` | `CTYPE`, `CALENDARID` | [`ABSCALENDAR`](../PLATFORM/ABSCALENDAR.md) | `CTYPE`, `CALENDARID` | RESTRICT | `ABSCALENDARAUTH.CTYPE = ABSCALENDAR.CTYPE AND ABSCALENDARAUTH.CALENDARID = ABSCALENDAR.CALENDARID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSCALENDARAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CTYPE,
       t.CALENDARID,
       t.USERUSERID,
       t.COMPANYCODE,
       t.AUTHVIEW,
       t.AUTHCREATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSCALENDARAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
