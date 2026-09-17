# DB2ADMIN.GATEPASS

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `GATEPASSNO`, `SHIFTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166340

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `GATEPASSNO` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 3 | `GATEPASSDATE` | DATE | NOT NULL |  |  |  |
| 4 | `SHIFTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `OUTTIME` | TIME | NOT NULL |  |  |  |
| 6 | `INTIME` | TIME | NOT NULL |  |  |  |
| 7 | `REASON` | CHAR(100) | NOT NULL |  |  |  |
| 8 | `ACTUALOUTTIME` | TIME |  |  |  |  |
| 9 | `ACTUALINTIME` | TIME |  |  |  |  |
| 10 | `NOOFHRS` | TIME |  |  |  |  |
| 11 | `PAYMENT` | INTEGER | NOT NULL |  |  |  |
| 12 | `AUTHORIZATION` | INTEGER | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GATEPASS.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GATEPASS.COMPANYCODE = EMPLOYEE.COMPANYCODE AND GATEPASS.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `SHIFT_SHIFT` | `COMPANYCODE`, `SHIFTCODE` | [`SHIFT`](../HR/SHIFT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GATEPASS.COMPANYCODE = SHIFT.COMPANYCODE AND GATEPASS.SHIFTCODE = SHIFT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GATEPASSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.GATEPASSNO,
       t.GATEPASSDATE,
       t.SHIFTCODE,
       t.OUTTIME,
       t.INTIME,
       t.REASON,
       t.ACTUALOUTTIME,
       t.ACTUALINTIME,
       t.NOOFHRS,
       t.PAYMENT
FROM   DB2ADMIN.GATEPASS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
