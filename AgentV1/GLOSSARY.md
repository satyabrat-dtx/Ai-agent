# Column glossary (inferred)

The source DDL has **no `COMMENT ON` statements**, so nothing here is declared by
the database. Each entry below is inferred from the column's name, its type, the
tables it appears in, and the foreign keys it participates in.

Treat these as hints for choosing columns, not as documented semantics.

| Column | Tables | Inferred meaning |
|---|---|---|
| `ABSUNIQUEID` | 2896 | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| `CODE` | 932 | Business (natural) key of a master-data table, typically the last primary-key column. |
| `COMPANYCODE` | 1934 | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| `CREATIONDATETIME` | 2097 | Local-time creation timestamp (audit). |
| `CREATIONDATETIMEUTC` | 1941 | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| `CREATIONUSER` | 2243 | User who created the row (audit). |
| `DIVISIONCODE` | 639 | Division within a company; second-level organisational discriminator. |
| `FATHERID` | 541 | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| `FROMDATE` | 93 | Inclusive start of a validity period. |
| `IMPORTAUTOCOUNTER` | 319 | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| `IMPORTSTATUS` | 330 | Staging-row processing status (integration inbox pattern). |
| `LASTUPDATEDATETIME` | 2096 | Local-time last-modification timestamp (audit). |
| `LASTUPDATEDATETIMEUTC` | 1941 | UTC last-modification timestamp (audit). |
| `LASTUPDATEUSER` | 2096 | User who last modified the row (audit). |
| `LOGOPERATION` | 335 | Kind of audited change -- insert/update/delete (change-log table). |
| `LOGTIMESTAMP` | 336 | When the audited change was recorded (change-log table). |
| `LOGUSER` | 335 | User responsible for the audited change (change-log table). |
| `LONGDESCRIPTION` | 676 | Long human-readable label. |
| `NEXTRETRY` | 325 | Next retry timestamp for a failed staging row. |
| `RETRYNR` | 322 | Retry attempt counter for a staging row. |
| `SEARCHDESCRIPTION` | 671 | Normalised/uppercased label used for lookup and search screens. |
| `SHORTDESCRIPTION` | 681 | Short human-readable label. |
| `TODATE` | 82 | End of a validity period. |
| `UUID` | 331 | Externally-generated unique identifier, used for integration correlation. |
| `VALIDFROM` | 3 | Inclusive start of a validity period. |
| `VALIDTO` | 0 | End of a validity period. |
| `WSOPERATION` | 319 | Requested web-service operation for a staging row (integration inbox pattern). |

## How to interpret an unlisted column

1. Check whether it is part of a foreign key on the table's card — if so, its
   meaning is "reference to *that* parent", regardless of its name.
2. Decompose the name against the conventions in [`CONVENTIONS.md`](CONVENTIONS.md).
3. Check `catalog/column_index.json` to see which other tables use the same
   column name; a column on many tables is usually a framework or reference
   concept, one on a single table is usually domain-specific.
4. If it is still unclear, say so rather than guessing in a user-facing answer.
