# DB2ADMIN.FMGMASTER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `FMGCODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156602

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FMGCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `SERAILNO` | DECIMAL(11,0) |  |  |  |  |
| 6 | `ISSUESTARTDATE` | DATE | NOT NULL |  |  |  |
| 7 | `ISSUEENDDATE` | DATE |  |  |  |  |
| 8 | `DEPRECIATIONAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SCRAPDETAILSREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SCRAPDATE` | DATE |  |  |  |  |
| 11 | `SCRAPREASON` | CHAR(100) |  |  |  |  |
| 12 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FMGMASTER.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FMGMASTER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND FMGMASTER.APPROVEDBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FMGMASTER_FMGCODE` | [`FMGISSUERETURN`](../HR/FMGISSUERETURN.md) | `COMPANYCODE`, `FMGCODEFMGCODE` | `FMGISSUERETURN.COMPANYCODE = FMGMASTER.COMPANYCODE AND FMGISSUERETURN.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |
| `FMGMASTER_FMGCODE` | [`FMGSETTLEMENT`](../HR/FMGSETTLEMENT.md) | `COMPANYCODE`, `FMGCODEFMGCODE` | `FMGSETTLEMENT.COMPANYCODE = FMGMASTER.COMPANYCODE AND FMGSETTLEMENT.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |
| `FMGMASTER_FMGCODE` | [`TEMPFMGSETTLEMENT`](../HR/TEMPFMGSETTLEMENT.md) | `COMPANYCODE`, `FMGCODEFMGCODE` | `TEMPFMGSETTLEMENT.COMPANYCODE = FMGMASTER.COMPANYCODE AND TEMPFMGSETTLEMENT.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |

## Indexes

- `FMGMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FMGCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SERAILNO,
       t.ISSUESTARTDATE,
       t.ISSUEENDDATE,
       t.DEPRECIATIONAPPLICABLE,
       t.SCRAPDETAILSREQUIRED,
       t.SCRAPDATE,
       t.SCRAPREASON
FROM   DB2ADMIN.FMGMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
