# DB2ADMIN.ICITEMTYPELEVMAPDEST

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ICITEMTYPELEVMAPORICMPCOD`, `CITEMTYPELEVMAPORIITCOD`, `DESTINATIONCOMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213592

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ICITEMTYPELEVMAPORICMPCOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CITEMTYPELEVMAPORIITCOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DESTINATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DESTINATIONITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `DESTINATIONITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCOMPANY_DESTINATIONCOMPANY` | `DESTINATIONCOMPANYCODE` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `CODE` | RESTRICT | `ICITEMTYPELEVMAPDEST.DESTINATIONCOMPANYCODE = ABSCOMPANY.CODE` |
| `ICITEMTYPELEVMAPORI_DESTINATIONS` | `ICITEMTYPELEVMAPORICMPCOD`, `CITEMTYPELEVMAPORIITCOD` | [`ICITEMTYPELEVMAPORI`](../PLATFORM/ICITEMTYPELEVMAPORI.md) | `COMPANYCODE`, `ITEMTYPECODE` | RESTRICT | `ICITEMTYPELEVMAPDEST.ICITEMTYPELEVMAPORICMPCOD = ICITEMTYPELEVMAPORI.COMPANYCODE AND ICITEMTYPELEVMAPDEST.CITEMTYPELEVMAPORIITCOD = ICITEMTYPELEVMAPORI.ITEMTYPECODE` |
| `ITEMTYPE_DESTINATIONITEMTYPE` | `DESTINATIONITEMTYPECOMPANYCODE`, `DESTINATIONITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ICITEMTYPELEVMAPDEST.DESTINATIONITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ICITEMTYPELEVMAPDEST.DESTINATIONITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ICITEMTYPELEVMAPDESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ICITEMTYPELEVMAPORICMPCOD,
       t.CITEMTYPELEVMAPORIITCOD,
       t.DESTINATIONCOMPANYCODE,
       t.DESTINATIONITEMTYPECOMPANYCODE,
       t.DESTINATIONITEMTYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ICITEMTYPELEVMAPDEST t
FETCH FIRST 100 ROWS ONLY;
```
