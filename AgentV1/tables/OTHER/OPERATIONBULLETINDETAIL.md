# DB2ADMIN.OPERATIONBULLETINDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `OGUSERGENERICGROUPTYPECODE`, `OGCODE`, `OPERATIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127203

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `OGUSERGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `OGUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `OGCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `OPERATIONCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `OPERATIONDESC` | CHAR(100) |  |  |  |  |
| 7 | `STM` | DECIMAL(7,3) | NOT NULL |  |  |  |
| 8 | `DIRECTINDIRECT` | CHAR(1) |  |  |  |  |
| 9 | `MCTEUSERGENGRPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `MCTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `MCTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 12 | `TEMPATTACHMENT` | CHAR(5) |  |  |  |  |
| 13 | `ATTACHMENTUSERGENGRPTECMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ATTACHMENTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `OPERATIONBULLETINDETAIL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `OPERATIONBULLETINDETAIL.COMPANYCODE = DIVISION.COMPANYCODE AND OPERATIONBULLETINDETAIL.DIVISIONCODE = DIVISION.CODE` |
| `USERGENERICGROUP_ATTACHMENT` | `ATTACHMENTUSERGENGRPTECMYCODE`, `DIVISIONCODE`, `ATTACHMENTCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `OPERATIONBULLETINDETAIL.ATTACHMENTUSERGENGRPTECMYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND OPERATIONBULLETINDETAIL.DIVISIONCODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND OPERATIONBULLETINDETAIL.ATTACHMENTCODE = USERGENERICGROUP.CODE` |
| `USERGENERICGROUP_MCTYPE` | `MCTEUSERGENGRPTYPECOMPANYCODE`, `MCTYPEUSERGENERICGROUPTYPECODE`, `MCTYPECODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `OPERATIONBULLETINDETAIL.MCTEUSERGENGRPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND OPERATIONBULLETINDETAIL.MCTYPEUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND OPERATIONBULLETINDETAIL.MCTYPECODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `OPERATIONBULLETINDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.OGUSERGENGROUPTYPECOMPANYCODE,
       t.OGUSERGENERICGROUPTYPECODE,
       t.OGCODE,
       t.OPERATIONCODE,
       t.OPERATIONDESC,
       t.STM,
       t.DIRECTINDIRECT,
       t.MCTEUSERGENGRPTYPECOMPANYCODE,
       t.MCTYPEUSERGENERICGROUPTYPECODE,
       t.MCTYPECODE
FROM   DB2ADMIN.OPERATIONBULLETINDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
