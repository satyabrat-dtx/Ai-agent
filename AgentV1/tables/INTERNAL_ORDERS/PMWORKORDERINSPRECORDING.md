# DB2ADMIN.PMWORKORDERINSPRECORDING

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `PMWORKORDERCOUNTERCODE`, `PMWORKORDERCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89260

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PMWORKORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMWORKORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PMBOMCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `PMBOMCODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `VALUE` | DECIMAL(20,5) |  |  |  |  |
| 10 | `REMARKS` | CHAR(50) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMWORKORDERINSPRECORDING.COMPANYCODE = COMPANY.CODE` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMWORKORDERINSPRECORDING.COMPANYCODE = PMBOM.COMPANYCODE AND PMWORKORDERINSPRECORDING.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMWORKORDERINSPRECORDING.PMBOMCODE = PMBOM.CODE` |
| `PMWORKORDER_PMWORKORDER` | `COMPANYCODE`, `PMWORKORDERCOUNTERCODE`, `PMWORKORDERCODE` | [`PMWORKORDER`](../INTERNAL_ORDERS/PMWORKORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMWORKORDERINSPRECORDING.COMPANYCODE = PMWORKORDER.COMPANYCODE AND PMWORKORDERINSPRECORDING.PMWORKORDERCOUNTERCODE = PMWORKORDER.COUNTERCODE AND PMWORKORDERINSPRECORDING.PMWORKORDERCODE = PMWORKORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMWORKORDERINSPRECORDINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PMWORKORDERCOUNTERCODE,
       t.PMWORKORDERCODE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.LINENO,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.VALUE,
       t.REMARKS,
       t.CREATIONDATETIME
FROM   DB2ADMIN.PMWORKORDERINSPRECORDING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
