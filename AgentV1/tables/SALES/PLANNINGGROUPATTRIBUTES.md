# DB2ADMIN.PLANNINGGROUPATTRIBUTES

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `PLANNINGGROUPINGCOMPANYCODE`, `PLANNINGGROUPINGCODE`, `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206596

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANNINGGROUPINGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLANNINGGROUPINGCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `GRPSUBCODE01` | SMALLINT | NOT NULL |  |  |  |
| 5 | `GRPSUBCODE02` | SMALLINT | NOT NULL |  |  |  |
| 6 | `GRPSUBCODE03` | SMALLINT | NOT NULL |  |  |  |
| 7 | `GRPSUBCODE04` | SMALLINT | NOT NULL |  |  |  |
| 8 | `GRPSUBCODE05` | SMALLINT | NOT NULL |  |  |  |
| 9 | `GRPSUBCODE06` | SMALLINT | NOT NULL |  |  |  |
| 10 | `GRPSUBCODE07` | SMALLINT | NOT NULL |  |  |  |
| 11 | `GRPSUBCODE08` | SMALLINT | NOT NULL |  |  |  |
| 12 | `GRPSUBCODE09` | SMALLINT | NOT NULL |  |  |  |
| 13 | `GRPSUBCODE10` | SMALLINT | NOT NULL |  |  |  |
| 14 | `GROUPPERREQUIREDDATE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PLANNINGGROUPING_GROUPATTRIBUTES` | `PLANNINGGROUPINGCOMPANYCODE`, `PLANNINGGROUPINGCODE` | [`PLANNINGGROUPING`](../SALES/PLANNINGGROUPING.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLANNINGGROUPATTRIBUTES.PLANNINGGROUPINGCOMPANYCODE = PLANNINGGROUPING.COMPANYCODE AND PLANNINGGROUPATTRIBUTES.PLANNINGGROUPINGCODE = PLANNINGGROUPING.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANNINGGROUPATTRIBUTESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PLANNINGGROUPINGCOMPANYCODE,
       t.PLANNINGGROUPINGCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.GRPSUBCODE01,
       t.GRPSUBCODE02,
       t.GRPSUBCODE03,
       t.GRPSUBCODE04,
       t.GRPSUBCODE05,
       t.GRPSUBCODE06,
       t.GRPSUBCODE07,
       t.GRPSUBCODE08
FROM   DB2ADMIN.PLANNINGGROUPATTRIBUTES t
FETCH FIRST 100 ROWS ONLY;
```
