# DB2ADMIN.RG23IICTAX

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `RG23IICCOMPANYCODE`, `RG23IICEXCISEYEARREGNO`, `RG23IICEXCISEYEARCODE`, `RG23IICCODE`, `ITAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RG23IICCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RG23IICEXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RG23IICEXCISEYEARCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RG23IICCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 7 | `MODVATCYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 9 | `MODVATNYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RG23IIC_TAXES` | `RG23IICCOMPANYCODE`, `RG23IICEXCISEYEARREGNO`, `RG23IICEXCISEYEARCODE`, `RG23IICCODE` | [`RG23IIC`](../OTHER/RG23IIC.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `CODE` | RESTRICT | `RG23IICTAX.RG23IICCOMPANYCODE = RG23IIC.COMPANYCODE AND RG23IICTAX.RG23IICEXCISEYEARREGNO = RG23IIC.EXCISEYEARREGNO AND RG23IICTAX.RG23IICEXCISEYEARCODE = RG23IIC.EXCISEYEARCODE AND RG23IICTAX.RG23IICCODE = RG23IIC.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG23IICTAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RG23IICCOMPANYCODE,
       t.RG23IICEXCISEYEARREGNO,
       t.RG23IICEXCISEYEARCODE,
       t.RG23IICCODE,
       t.ITAXCODE,
       t.AMOUNT,
       t.MODVATCYPERCENTAGE,
       t.MODVATCYVALUE,
       t.MODVATNYPERCENTAGE,
       t.MODVATNYVALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RG23IICTAX t
FETCH FIRST 100 ROWS ONLY;
```
