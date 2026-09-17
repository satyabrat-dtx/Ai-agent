# DB2ADMIN.ALTERNATIVEPRODUCTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 36
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210763

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `VALIDITYSTATUS` | CHAR(2) |  |  |  |  |
| 6 | `CREATIONCONTEXT` | INTEGER | NOT NULL |  |  |  |
| 7 | `ORIGINALITEMFULLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 9 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 11 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `OBSOLETEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 25 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 28 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 34 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 35 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ALTERNATIVEPRODUCTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.ENTITYNAME,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.VALIDITYSTATUS,
       t.CREATIONCONTEXT,
       t.ORIGINALITEMFULLREQUIRED,
       t.ITEMTYPEAFICODE,
       t.PROTOTYPE,
       t.PROTOTYPEPROJECT,
       t.PROTOTYPEVERSION
FROM   DB2ADMIN.ALTERNATIVEPRODUCTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
