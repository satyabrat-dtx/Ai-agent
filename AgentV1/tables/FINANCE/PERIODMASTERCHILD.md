# DB2ADMIN.PERIODMASTERCHILD

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `PERIODMASTERCOMPANYCODE`, `PERIODMASTERDIVISIONCODE`, `PERIODMASTERMODUL`, `PERIODMASTERINFOTYPECODE`, `PERIODMASTERFISCALYEAR`, `PERIODMASTERABBREVFISCALYEAR`, `PERIOD`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103080

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PERIODMASTERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PERIODMASTERDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PERIODMASTERMODUL` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PERIODMASTERINFOTYPECODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PERIODMASTERFISCALYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PERIODMASTERABBREVFISCALYEAR` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `NAME` | CHAR(30) | NOT NULL |  |  |  |
| 8 | `INITIALDATE` | DATE |  |  |  |  |
| 9 | `FINALDATE` | DATE |  |  |  |  |
| 10 | `POSTINGVALIDITY` | INTEGER | NOT NULL |  |  |  |
| 11 | `SALESTAXREPORTED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SALESTAXREPORTEDINFO` | CHAR(100) |  |  |  |  |
| 13 | `JOURNALSTATUS` | CHAR(1) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PERIODMASTER_PERIODS` | `PERIODMASTERCOMPANYCODE`, `PERIODMASTERDIVISIONCODE`, `PERIODMASTERMODUL`, `PERIODMASTERINFOTYPECODE`, `PERIODMASTERFISCALYEAR`, `PERIODMASTERABBREVFISCALYEAR` | [`PERIODMASTER`](../FINANCE/PERIODMASTER.md) | `COMPANYCODE`, `DIVISIONCODE`, `MODUL`, `INFOTYPECODE`, `FISCALYEAR`, `ABBREVFISCALYEAR` | RESTRICT | `PERIODMASTERCHILD.PERIODMASTERCOMPANYCODE = PERIODMASTER.COMPANYCODE AND PERIODMASTERCHILD.PERIODMASTERDIVISIONCODE = PERIODMASTER.DIVISIONCODE AND PERIODMASTERCHILD.PERIODMASTERMODUL = PERIODMASTER.MODUL AND PERIODMASTERCHILD.PERIODMASTERINFOTYPECODE = PERIODMASTER.INFOTYPECODE AND PERIODMASTERCHILD.PERIODMASTERFISCALYEAR = PERIODMASTER.FISCALYEAR AND PERIODMASTERCHILD.PERIODMASTERABBREVFISCALYEAR = PERIODMASTER.ABBREVFISCALYEAR` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PERIODMASTERCHILDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PERIODMASTERCOMPANYCODE,
       t.PERIODMASTERDIVISIONCODE,
       t.PERIODMASTERMODUL,
       t.PERIODMASTERINFOTYPECODE,
       t.PERIODMASTERFISCALYEAR,
       t.PERIODMASTERABBREVFISCALYEAR,
       t.PERIOD,
       t.NAME,
       t.INITIALDATE,
       t.FINALDATE,
       t.POSTINGVALIDITY,
       t.SALESTAXREPORTED
FROM   DB2ADMIN.PERIODMASTERCHILD t
FETCH FIRST 100 ROWS ONLY;
```
