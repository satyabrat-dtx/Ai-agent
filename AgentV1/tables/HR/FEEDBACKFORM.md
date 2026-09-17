# DB2ADMIN.FEEDBACKFORM

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE`, `PARTICIPANTEMPLOYEEIDCODE`, `TRAINERCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 153192

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRAININGTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TRAININGTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TRAININGCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PARTICIPANTEMPLOYEEIDCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 5 | `TRAINERCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 6 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 7 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 8 | `CONTENTSA` | INTEGER | NOT NULL |  |  |  |
| 9 | `CONTENTSB` | INTEGER | NOT NULL |  |  |  |
| 10 | `CONTENTSC` | INTEGER | NOT NULL |  |  |  |
| 11 | `FACULITYA` | INTEGER | NOT NULL |  |  |  |
| 12 | `FACULITYB` | INTEGER | NOT NULL |  |  |  |
| 13 | `FACULITYC` | INTEGER | NOT NULL |  |  |  |
| 14 | `METHODOLOGYA` | INTEGER | NOT NULL |  |  |  |
| 15 | `METHODOLOGYB` | INTEGER | NOT NULL |  |  |  |
| 16 | `METHODOLOGYC` | INTEGER | NOT NULL |  |  |  |
| 17 | `RELEVANCETOYOURROLEA` | INTEGER | NOT NULL |  |  |  |
| 18 | `RELEVANCETOYOURROLEB` | INTEGER | NOT NULL |  |  |  |
| 19 | `RELEVANCETOYOURROLEC` | INTEGER | NOT NULL |  |  |  |
| 20 | `RELEVANCETOYOURROLED` | INTEGER | NOT NULL |  |  |  |
| 21 | `RELEVANCETOYOURROLEE` | INTEGER | NOT NULL |  |  |  |
| 22 | `MOSTUSEFULL` | CHAR(100) |  |  |  |  |
| 23 | `LEASTUSEFULL` | CHAR(100) |  |  |  |  |
| 24 | `OMITFROMTHECOURSE` | CHAR(100) |  |  |  |  |
| 25 | `COMMENTS` | CHAR(100) |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FEEDBACKFORM.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_TRAININGTYPE` | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `FEEDBACKFORM.COMPANYCODE = ICSENTITY.COMPANYCODE AND FEEDBACKFORM.TRAININGTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND FEEDBACKFORM.TRAININGTYPECODE = ICSENTITY.CODE` |
| `TRAINING_TRAINING` | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE` | [`TRAINING`](../HR/TRAINING.md) | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `CODE` | RESTRICT | `FEEDBACKFORM.COMPANYCODE = TRAINING.COMPANYCODE AND FEEDBACKFORM.TRAININGTYPEICSTABLECODE = TRAINING.TRAININGTYPEICSTABLECODE AND FEEDBACKFORM.TRAININGTYPECODE = TRAINING.TRAININGTYPECODE AND FEEDBACKFORM.TRAININGCODE = TRAINING.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FEEDBACKFORMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRAININGTYPEICSTABLECODE,
       t.TRAININGTYPECODE,
       t.TRAININGCODE,
       t.PARTICIPANTEMPLOYEEIDCODE,
       t.TRAINERCODE,
       t.FROMDATE,
       t.TODATE,
       t.CONTENTSA,
       t.CONTENTSB,
       t.CONTENTSC,
       t.FACULITYA
FROM   DB2ADMIN.FEEDBACKFORM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
