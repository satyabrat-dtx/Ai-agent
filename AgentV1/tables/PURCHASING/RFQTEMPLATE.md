# DB2ADMIN.RFQTEMPLATE

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109722

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `FULLITEMREQD` | SMALLINT | NOT NULL |  |  |  |
| 10 | `DELIVERYDATE` | CHAR(1) |  |  |  |  |
| 11 | `BASEPRICE` | CHAR(3) |  |  |  |  |
| 12 | `TYPEOFAPPROVAL` | CHAR(1) |  |  |  |  |
| 13 | `DIVISIONWISE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `MERGEDDAYS` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RFQTEMPLATE.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND RFQTEMPLATE.COUNTERCODE = COUNTER.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RFQTEMPLATE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RFQTEMPLATE.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RFQTEMPLATE_RFQTEMPLATE` | [`RFQHEADER`](../PURCHASING/RFQHEADER.md) | `COMPANYCODE`, `RFQTEMPLATECODE` | `RFQHEADER.COMPANYCODE = RFQTEMPLATE.COMPANYCODE AND RFQHEADER.RFQTEMPLATECODE = RFQTEMPLATE.CODE` |

## Indexes

- `RFQTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.FULLITEMREQD,
       t.DELIVERYDATE,
       t.BASEPRICE
FROM   DB2ADMIN.RFQTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
