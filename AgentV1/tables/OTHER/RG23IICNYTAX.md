# DB2ADMIN.RG23IICNYTAX

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `RG23IICNYCOMPANYCODE`, `RG23IICNYEXCISEYEARREGNO`, `RG23IICNYEXCISEYEARCODE`, `RG23IICNYCODE`, `ITAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143263

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RG23IICNYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RG23IICNYEXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RG23IICNYEXCISEYEARCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RG23IICNYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 7 | `MODVATCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 9 | `MODVATNYVALUE` | DECIMAL(18,5) |  |  |  |  |
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
| `RG23IICNY_TAXES` | `RG23IICNYCOMPANYCODE`, `RG23IICNYEXCISEYEARREGNO`, `RG23IICNYEXCISEYEARCODE`, `RG23IICNYCODE` | [`RG23IICNY`](../OTHER/RG23IICNY.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `CODE` | RESTRICT | `RG23IICNYTAX.RG23IICNYCOMPANYCODE = RG23IICNY.COMPANYCODE AND RG23IICNYTAX.RG23IICNYEXCISEYEARREGNO = RG23IICNY.EXCISEYEARREGNO AND RG23IICNYTAX.RG23IICNYEXCISEYEARCODE = RG23IICNY.EXCISEYEARCODE AND RG23IICNYTAX.RG23IICNYCODE = RG23IICNY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG23IICNYTAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RG23IICNYCOMPANYCODE,
       t.RG23IICNYEXCISEYEARREGNO,
       t.RG23IICNYEXCISEYEARCODE,
       t.RG23IICNYCODE,
       t.ITAXCODE,
       t.AMOUNT,
       t.MODVATCYPERCENTAGE,
       t.MODVATCYVALUE,
       t.MODVATNYPERCENTAGE,
       t.MODVATNYVALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RG23IICNYTAX t
FETCH FIRST 100 ROWS ONLY;
```
