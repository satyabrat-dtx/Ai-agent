# DB2ADMIN.TRANSACTIONALNUMBERING

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7892

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COUNTERTYPECODE` | CHAR(2) |  | FK | foreign_key |  |
| 6 | `TRANSIENTCOUNTER` | SMALLINT | NOT NULL |  |  |  |
| 7 | `DEFAULTCOUNTER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `NUMERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SUBSERIESREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBSERIESTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `BEGINNINGLIMIT` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 13 | `FINALLIMIT` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 14 | `NUMERATIONSTEP` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 15 | `MASK` | VARCHAR(100) | NOT NULL |  |  |  |
| 16 | `OUTPUTSEPARATOR` | CHAR(1) |  |  |  |  |
| 17 | `COUNTERWIDTH` | INTEGER | NOT NULL |  |  |  |
| 18 | `SUBSERIESCODEWIDTH` | INTEGER | NOT NULL |  |  |  |
| 19 | `PREFIX` | VARCHAR(80) |  |  |  |  |
| 20 | `SUFFIX` | VARCHAR(80) |  |  |  |  |
| 21 | `COUNTERRESETFORERASE` | SMALLINT | NOT NULL |  |  |  |
| 22 | `RULESRESPECT` | CHAR(2) | NOT NULL |  |  |  |
| 23 | `EVENTSSEQUENTIALITY` | CHAR(2) | NOT NULL |  |  |  |
| 24 | `UPDATEFORMANUSING` | INTEGER | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRANSACTIONALNUMBERING.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRANSACTIONALNUMBERING.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COUNTERTYPE_COUNTERTYPE` | `COUNTERTYPECODE` | [`COUNTERTYPE`](../CORE_MASTER/COUNTERTYPE.md) | `CODE` | RESTRICT | `TRANSACTIONALNUMBERING.COUNTERTYPECODE = COUNTERTYPE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRANSACTIONALNUMBERING_SUBSERIES` | [`TRNUMBERINGSUBSERIES`](../WAREHOUSE/TRNUMBERINGSUBSERIES.md) | `TRANSACTIONALNUMBERINGCMYCODE`, `TRANSACTIONALNUMBERINGCODE` | `TRNUMBERINGSUBSERIES.TRANSACTIONALNUMBERINGCMYCODE = TRANSACTIONALNUMBERING.COMPANYCODE AND TRNUMBERINGSUBSERIES.TRANSACTIONALNUMBERINGCODE = TRANSACTIONALNUMBERING.CODE` |
| `TRANSACTIONALNUMBERING_DEFINITIVEELEMENTNUMBERING` | [`BASECUSTOMIZEDOPTIONS`](../FINANCE/BASECUSTOMIZEDOPTIONS.md) | `DEFINITIVEELMNUMBERINGCMYCODE`, `DEFINITIVEELEMENTNUMBERINGCODE` | `BASECUSTOMIZEDOPTIONS.DEFINITIVEELMNUMBERINGCMYCODE = TRANSACTIONALNUMBERING.COMPANYCODE AND BASECUSTOMIZEDOPTIONS.DEFINITIVEELEMENTNUMBERINGCODE = TRANSACTIONALNUMBERING.CODE` |
| `TRANSACTIONALNUMBERING_DEFINITIVETRANSACTIONNUMBERING` | [`WAREHOUSECUSTOMIZEDOPTIONS`](../WAREHOUSE/WAREHOUSECUSTOMIZEDOPTIONS.md) | `DEFINITIVETRNNUMBERINGCMYCODE`, `DEFINITIVETRNNUMBERINGCODE` | `WAREHOUSECUSTOMIZEDOPTIONS.DEFINITIVETRNNUMBERINGCMYCODE = TRANSACTIONALNUMBERING.COMPANYCODE AND WAREHOUSECUSTOMIZEDOPTIONS.DEFINITIVETRNNUMBERINGCODE = TRANSACTIONALNUMBERING.CODE` |

## Indexes

- `TRANSACTIONALNUMBERINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNTERTYPECODE,
       t.TRANSIENTCOUNTER,
       t.DEFAULTCOUNTER,
       t.NUMERATIONTYPE,
       t.SUBSERIESREQUIRED,
       t.SUBSERIESTYPE,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.TRANSACTIONALNUMBERING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
