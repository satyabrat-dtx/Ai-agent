# DB2ADMIN.TRAINING

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161349

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRAININGTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TRAININGTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(6) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAINING.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_TRAININGTYPE` | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAINING.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAINING.TRAININGTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAINING.TRAININGTYPECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAINING_TRAINING` | [`FEEDBACKFORM`](../HR/FEEDBACKFORM.md) | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE` | `FEEDBACKFORM.COMPANYCODE = TRAINING.COMPANYCODE AND FEEDBACKFORM.TRAININGTYPEICSTABLECODE = TRAINING.TRAININGTYPEICSTABLECODE AND FEEDBACKFORM.TRAININGTYPECODE = TRAINING.TRAININGTYPECODE AND FEEDBACKFORM.TRAININGCODE = TRAINING.CODE` |
| `TRAINING_TRAINING` | [`TRAININGNOMINATION`](../HR/TRAININGNOMINATION.md) | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE` | `TRAININGNOMINATION.COMPANYCODE = TRAINING.COMPANYCODE AND TRAININGNOMINATION.TRAININGTYPEICSTABLECODE = TRAINING.TRAININGTYPEICSTABLECODE AND TRAININGNOMINATION.TRAININGTYPECODE = TRAINING.TRAININGTYPECODE AND TRAININGNOMINATION.TRAININGCODE = TRAINING.CODE` |
| `TRAINING_TRAINING` | [`TRAININGSCHEDULE`](../HR/TRAININGSCHEDULE.md) | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE` | `TRAININGSCHEDULE.COMPANYCODE = TRAINING.COMPANYCODE AND TRAININGSCHEDULE.TRAININGTYPEICSTABLECODE = TRAINING.TRAININGTYPEICSTABLECODE AND TRAININGSCHEDULE.TRAININGTYPECODE = TRAINING.TRAININGTYPECODE AND TRAININGSCHEDULE.TRAININGCODE = TRAINING.CODE` |
| `TRAINING_TRAINING` | [`ESSTRAININGNOMINATION`](../HR/ESSTRAININGNOMINATION.md) | `COMPANYCODE`, `TRAININGTYPEICSTABLECODE`, `TRAININGTYPECODE`, `TRAININGCODE` | `ESSTRAININGNOMINATION.COMPANYCODE = TRAINING.COMPANYCODE AND ESSTRAININGNOMINATION.TRAININGTYPEICSTABLECODE = TRAINING.TRAININGTYPEICSTABLECODE AND ESSTRAININGNOMINATION.TRAININGTYPECODE = TRAINING.TRAININGTYPECODE AND ESSTRAININGNOMINATION.TRAININGCODE = TRAINING.CODE` |

## Indexes

- `TRAININGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRAININGTYPEICSTABLECODE,
       t.TRAININGTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.TRAINING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
