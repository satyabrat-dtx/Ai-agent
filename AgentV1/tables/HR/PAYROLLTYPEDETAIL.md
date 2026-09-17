# DB2ADMIN.PAYROLLTYPEDETAIL

- **Module**: `HR` (high confidence — table name starts with 'PAYROLL')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `PAYROLLTYPECOMPANYCODE`, `PAYROLLTYPECODE`, `ATTENDANCETYPECODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 155452

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PAYROLLTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PAYROLLTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `PAYROLLTYPECOMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PAYROLLTYPEDETAIL.PAYROLLTYPECOMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND PAYROLLTYPEDETAIL.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `PAYROLLTYPE_LINE` | `PAYROLLTYPECOMPANYCODE`, `PAYROLLTYPECODE` | [`PAYROLLTYPE`](../HR/PAYROLLTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PAYROLLTYPEDETAIL.PAYROLLTYPECOMPANYCODE = PAYROLLTYPE.COMPANYCODE AND PAYROLLTYPEDETAIL.PAYROLLTYPECODE = PAYROLLTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PAYROLLTYPEDETAIL_ATTDTYPE` | [`ATTENDANCECORRECTION`](../HR/ATTENDANCECORRECTION.md) | `COMPANYCODE`, `PAYROLLCODE`, `ATTDTYPEATTENDANCETYPECODE` | `ATTENDANCECORRECTION.COMPANYCODE = PAYROLLTYPEDETAIL.PAYROLLTYPECOMPANYCODE AND ATTENDANCECORRECTION.PAYROLLCODE = PAYROLLTYPEDETAIL.PAYROLLTYPECODE AND ATTENDANCECORRECTION.ATTDTYPEATTENDANCETYPECODE = PAYROLLTYPEDETAIL.ATTENDANCETYPECODE` |

## Indexes

- `PAYROLLTYPEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PAYROLLTYPECOMPANYCODE,
       t.PAYROLLTYPECODE,
       t.ATTENDANCETYPECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.PAYROLLTYPEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
