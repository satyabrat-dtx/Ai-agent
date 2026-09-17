# DB2ADMIN.INVESTMENTGRPENTITY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `CODE`, `GROUPITEMCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157561

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | CHAR(100) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | CHAR(35) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | CHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `FLAGPERCENTAGEAMOUNT` | INTEGER | NOT NULL |  |  |  |
| 6 | `PERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 7 | `MAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `PRIORITYNUMBER` | INTEGER | NOT NULL |  |  |  |
| 9 | `TAXCODEREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 10 | `DECLARATIONALLOWED` | INTEGER | NOT NULL |  |  |  |
| 11 | `GROUPITEMCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `GRPLONGDESCR` | CHAR(100) |  |  |  |  |
| 13 | `GRPSHORTDESCR` | CHAR(35) |  |  |  |  |
| 14 | `GRPSEARCHDESCR` | CHAR(60) |  |  |  |  |
| 15 | `PAYELEMENTTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 16 | `PAYELEMENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 17 | `GRPITEMFLAGPERAMT` | INTEGER | NOT NULL |  |  |  |
| 18 | `GRPITEMPER` | DECIMAL(5,2) |  |  |  |  |
| 19 | `FLAGCALCULATED` | INTEGER | NOT NULL |  |  |  |
| 20 | `GRPITEMMAXAMT` | DECIMAL(17,2) |  |  |  |  |
| 21 | `GRPITEMPRIORITYNO` | INTEGER | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INVESTMENTGRPENTITY.COMPANYCODE = COMPANY.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `INVESTMENTGRPENTITY.COMPANYCODE = PAYELEMENT.COMPANYCODE AND INVESTMENTGRPENTITY.PAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND INVESTMENTGRPENTITY.PAYELEMENTCODE = PAYELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INVESTMENTGRPENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FLAGPERCENTAGEAMOUNT,
       t.PERCENTAGE,
       t.MAXAMOUNT,
       t.PRIORITYNUMBER,
       t.TAXCODEREQUIRED,
       t.DECLARATIONALLOWED,
       t.GROUPITEMCODE
FROM   DB2ADMIN.INVESTMENTGRPENTITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
