# DB2ADMIN.INSURANCEMASTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `INSURANCEAGENTCODEICSTABLECODE`, `INSURANCEAGENTCODECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157465

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INSURANCEAGENTCODEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INSURANCEAGENTCODECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYELEMENTPAYELEMENTTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 4 | `PAYELEMENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INSURANCEMASTER.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_INSURANCEAGENTCODE` | `COMPANYCODE`, `INSURANCEAGENTCODEICSTABLECODE`, `INSURANCEAGENTCODECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `INSURANCEMASTER.COMPANYCODE = ICSENTITY.COMPANYCODE AND INSURANCEMASTER.INSURANCEAGENTCODEICSTABLECODE = ICSENTITY.ICSTABLECODE AND INSURANCEMASTER.INSURANCEAGENTCODECODE = ICSENTITY.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTPAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `INSURANCEMASTER.COMPANYCODE = PAYELEMENT.COMPANYCODE AND INSURANCEMASTER.PAYELEMENTPAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND INSURANCEMASTER.PAYELEMENTCODE = PAYELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INSURANCEMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INSURANCEAGENTCODEICSTABLECODE,
       t.INSURANCEAGENTCODECODE,
       t.PAYELEMENTPAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.INSURANCEMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
