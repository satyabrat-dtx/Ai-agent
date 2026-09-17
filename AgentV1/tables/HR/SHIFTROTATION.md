# DB2ADMIN.SHIFTROTATION

- **Module**: `HR` (low confidence — FK neighbourhood: 3 of 3 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 7 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156167

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIFTROTATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 7

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SHIFTROTATION_WORKSHIFTNO` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `WORKSHIFTNOCODE` | `APPLICANTSDETAILS.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND APPLICANTSDETAILS.WORKSHIFTNOCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_WORKSHIFTNO` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `WORKSHIFTNOCODE` | `EMPLOYEE.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND EMPLOYEE.WORKSHIFTNOCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_WORKSHIFTNO` | [`EMPLOYEEHISTORY`](../HR/EMPLOYEEHISTORY.md) | `COMPANYCODE`, `WORKSHIFTNOCODE` | `EMPLOYEEHISTORY.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND EMPLOYEEHISTORY.WORKSHIFTNOCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_SHIFTROTATION` | [`EMPLOYEESHIFTROTATION`](../HR/EMPLOYEESHIFTROTATION.md) | `COMPANYCODE`, `SHIFTROTATIONCODE` | `EMPLOYEESHIFTROTATION.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND EMPLOYEESHIFTROTATION.SHIFTROTATIONCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_LINE` | [`SHIFTROTATIONDETAIL`](../HR/SHIFTROTATIONDETAIL.md) | `SHIFTROTATIONCOMPANYCODE`, `SHIFTROTATIONCODE` | `SHIFTROTATIONDETAIL.SHIFTROTATIONCOMPANYCODE = SHIFTROTATION.COMPANYCODE AND SHIFTROTATIONDETAIL.SHIFTROTATIONCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_WORKSHIFTNO` | [`ESSEMPLOYEE`](../HR/ESSEMPLOYEE.md) | `COMPANYCODE`, `WORKSHIFTNOCODE` | `ESSEMPLOYEE.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND ESSEMPLOYEE.WORKSHIFTNOCODE = SHIFTROTATION.CODE` |
| `SHIFTROTATION_CODE` | [`ESSEMPLOYEESHIFTROTATION`](../HR/ESSEMPLOYEESHIFTROTATION.md) | `COMPANYCODE`, `CODECODE` | `ESSEMPLOYEESHIFTROTATION.COMPANYCODE = SHIFTROTATION.COMPANYCODE AND ESSEMPLOYEESHIFTROTATION.CODECODE = SHIFTROTATION.CODE` |

## Indexes

- `SHIFTROTATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SHIFTROTATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
