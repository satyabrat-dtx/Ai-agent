# DB2ADMIN.PRLPOSTINGSUMMARYHEADER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `SNO`, `PAYROLLCODE`, `PROCESSPERIOD`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168155

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `STARTDATE` | DATE |  |  |  |  |
| 5 | `ENDDATE` | DATE |  |  |  |  |
| 6 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 7 | `FACTORYCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `FACTORYCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `BUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 10 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 11 | `FLAG` | CHAR(10) |  |  |  |  |
| 12 | `SAPMESSAGE` | VARCHAR(500) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 20 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 21 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRLPOSTINGSUMMARYHEADER.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYHEADER.COMPANYCODE = DIVISION.COMPANYCODE AND PRLPOSTINGSUMMARYHEADER.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYHEADER.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND PRLPOSTINGSUMMARYHEADER.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRLPOSTINGSUMMARYHEADER_LINE` | [`PRLPOSTINGSUMMARYDETAIL`](../HR/PRLPOSTINGSUMMARYDETAIL.md) | `PRLPOSTINGSUMMARYHDRCMYCODE`, `PRLPOSTINGSUMMARYHEADERSNO`, `PRLPOSTINGSUMMARYHDRPRCODE`, `PRLPOSTINGSUMMARYHDRPRPERIOD` | `PRLPOSTINGSUMMARYDETAIL.PRLPOSTINGSUMMARYHDRCMYCODE = PRLPOSTINGSUMMARYHEADER.COMPANYCODE AND PRLPOSTINGSUMMARYDETAIL.PRLPOSTINGSUMMARYHEADERSNO = PRLPOSTINGSUMMARYHEADER.SNO AND PRLPOSTINGSUMMARYDETAIL.PRLPOSTINGSUMMARYHDRPRCODE = PRLPOSTINGSUMMARYHEADER.PAYROLLCODE AND PRLPOSTINGSUMMARYDETAIL.PRLPOSTINGSUMMARYHDRPRPERIOD = PRLPOSTINGSUMMARYHEADER.PROCESSPERIOD` |

## Indexes

- `PRLPOSTINGSUMMARYHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SNO,
       t.PAYROLLCODE,
       t.PROCESSPERIOD,
       t.STARTDATE,
       t.ENDDATE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.BUSINESSAREACODE,
       t.POSTINGDATE,
       t.FLAG
FROM   DB2ADMIN.PRLPOSTINGSUMMARYHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
