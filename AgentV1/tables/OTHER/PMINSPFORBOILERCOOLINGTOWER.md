# DB2ADMIN.PMINSPFORBOILERCOOLINGTOWER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `INSPECTIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88919

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INSPECTIONCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 2 | `INSPECTIONDATE` | DATE | NOT NULL |  |  |  |
| 3 | `NUMERICFIELD1` | DECIMAL(15,5) |  |  |  |  |
| 4 | `NUMERICFIELD2` | DECIMAL(15,5) |  |  |  |  |
| 5 | `NUMERICFIELD3` | DECIMAL(15,5) |  |  |  |  |
| 6 | `NUMERICFIELD4` | DECIMAL(15,5) |  |  |  |  |
| 7 | `NUMERICFIELD5` | DECIMAL(15,5) |  |  |  |  |
| 8 | `NUMERICFIELD6` | DECIMAL(15,5) |  |  |  |  |
| 9 | `NUMERICFIELD7` | DECIMAL(15,5) |  |  |  |  |
| 10 | `NUMERICFIELD8` | DECIMAL(15,5) |  |  |  |  |
| 11 | `NUMERICFIELD9` | DECIMAL(15,5) |  |  |  |  |
| 12 | `NUMERICFIELD10` | DECIMAL(15,5) |  |  |  |  |
| 13 | `INSPECTIONTIME` | TIMESTAMP |  |  |  |  |
| 14 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 15 | `INSPECTEDBY` | CHAR(30) |  |  |  |  |
| 16 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 17 | `SHIFT` | CHAR(3) |  |  |  |  |
| 18 | `EMPLOYEECODE` | CHAR(10) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMINSPFORBOILERCOOLINGTOWER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NSPFORBOILERCOOLINGTOWERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INSPECTIONCODE,
       t.INSPECTIONDATE,
       t.NUMERICFIELD1,
       t.NUMERICFIELD2,
       t.NUMERICFIELD3,
       t.NUMERICFIELD4,
       t.NUMERICFIELD5,
       t.NUMERICFIELD6,
       t.NUMERICFIELD7,
       t.NUMERICFIELD8,
       t.NUMERICFIELD9
FROM   DB2ADMIN.PMINSPFORBOILERCOOLINGTOWER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
