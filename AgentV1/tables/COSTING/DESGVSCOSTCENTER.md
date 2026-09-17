# DB2ADMIN.DESGVSCOSTCENTER

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE`, `SHIFTCODE`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 150955

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DESIGNATIONICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DESIGNATIONCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SHIFTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 5 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 6 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `RATEPERDAY` | DECIMAL(7,2) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DESGVSCOSTCENTER.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESGVSCOSTCENTER.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND DESGVSCOSTCENTER.COSTCENTERCODE = COSTCENTER.CODE` |
| `ICSENTITY_DESIGNATION` | `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `DESGVSCOSTCENTER.COMPANYCODE = ICSENTITY.COMPANYCODE AND DESGVSCOSTCENTER.DESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND DESGVSCOSTCENTER.DESIGNATIONCODE = ICSENTITY.CODE` |
| `SHIFT_SHIFT` | `COMPANYCODE`, `SHIFTCODE` | [`SHIFT`](../HR/SHIFT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESGVSCOSTCENTER.COMPANYCODE = SHIFT.COMPANYCODE AND DESGVSCOSTCENTER.SHIFTCODE = SHIFT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESGVSCOSTCENTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DESIGNATIONICSTABLECODE,
       t.DESIGNATIONCODE,
       t.SHIFTCODE,
       t.FROMDATE,
       t.TODATE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.RATEPERDAY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.DESGVSCOSTCENTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
